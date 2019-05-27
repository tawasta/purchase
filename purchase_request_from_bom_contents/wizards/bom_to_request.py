from odoo import models, fields, api


class BomToRequest(models.TransientModel):

    _name = 'purchase_request_from_bom_contents.bom_to_request'
    _rec_name = 'bom_id'

    @api.multi
    def calculate_quantities(self):

        # Fetch quantities of all materials using the
        # mrp_bom_raw_material_quantities module.
        material_quantities \
            = self.bom_id \
            .compute_raw_material_qties(multiplier=self.multiplier)

        for material in material_quantities:
            self.env['purchase_request_from_bom_contents.bom_to_request_line']\
                .create({
                    'product_id': material['product'].id,
                    'uom_id': material['product'].uom_id.id,
                    'qty': material['quantity'],
                    'wizard_id': self.id,
                })

        # Reopen the wizard after state change
        self.state = 'qty_calculation'
        return {
            'context': self.env.context,
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'purchase_request_from_bom_contents.bom_to_request',
            'res_id': self.id,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'name': 'BOM To Purchase Request',
        }

    def get_request_line_values(self, line, purchase_request_id):
        # Override to provide extra values
        return {
            'product_id': line.product_id.id,
            'request_id': purchase_request_id,
        }

    def get_line_domain(self, line, purchase_request_id):
        return [('product_id', '=', line.product_id.id),
                ('product_uom_id', '=', line.uom_id.id),
                ('request_id', '=', purchase_request_id)]

    @api.multi
    def add_request_lines(self):
        purchase_request_line_model = self.env['purchase.request.line']
        purchase_request_id = self._context['active_id']

        for line in self.product_line_ids:
            args = self.get_line_domain(line, purchase_request_id)

            matching_request_line \
                = purchase_request_line_model.search(args=args, limit=1)

            if self.combine_with_existing and matching_request_line:
                matching_request_line[0].product_qty \
                    = matching_request_line[0].product_qty \
                    + (line.qty * self.multiplier)
            else:
                pr_line_values \
                    = self.get_request_line_values(line, purchase_request_id)

                res = purchase_request_line_model.create(pr_line_values)
                # Call onchange to get the full product description,
                # and add rest of the line info afterwards
                res.onchange_product_id()
                res.write({
                    'product_uom_id': line.uom_id.id,
                    'product_qty': line.qty * self.multiplier,
                })

    bom_id = fields.Many2one(
        comodel_name='mrp.bom',
        string='BOM'
    )

    product_line_ids = fields.One2many(
        comodel_name='purchase_request_from_bom_contents.bom_to_request_line',
        inverse_name='wizard_id',
        string='Components'
    )

    state = fields.Selection(
        selection=[('bom_selection', 'BOM Selection'),
                   ('qty_calculation', 'Quantity Calculation')],
        default='bom_selection'
    )

    multiplier = fields.Integer(
        string='Multiplier',
        default=1,
        help=('''Change this to e.g. 5 if you want to add 5 BOMs worth
              of components to the purchase request''')
    )

    combine_with_existing = fields.Boolean(
        string='Combine with existing Purchase Request lines',
        default=True,
        help=('''If the same product already exists on the Purchase Request,
              the quantities are merged.''')
    )
