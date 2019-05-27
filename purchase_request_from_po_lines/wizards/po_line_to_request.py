from odoo import models, fields, api, _, exceptions


class PoLineToRequest(models.TransientModel):

    _name = 'purchase_request_from_po_lines.po_line_to_request'
    _rec_name = 'analytic_account_id'

    @api.onchange('type')
    def onchange_type(self):

        purchase_request_model = self.env['purchase.request']

        if self.type == 'latest_own':
            res = purchase_request_model.search(
                args=[('requested_by', '=', self.env.uid),
                      ('state', 'in', ['draft', 'to_approve'])],
                limit=1,
                order='date_start DESC, id DESC')

            if not res:
                self.purchase_request_id = False
                self.type = 'new'
                txt = _("You don't have any Purchase Requests "
                        "that are in Draft or To Approve state.")
                raise exceptions.Warning(txt)
            else:
                self.purchase_request_id = res[0].id
        else:
            self.purchase_request_id = False

    @api.multi
    def create_purchase_request(self):
        '''Create a new purchase request containing the selected PO lines.'''

        purchase_request_model = self.env['purchase.request']
        purchase_request_line_model = self.env['purchase.request.line']
        purchase_order_line_model = self.env['purchase.order.line']

        if self.type == 'new':
            pr_vals = {
                'description': _('Created from Purchase Order Lines')
            }

            # If purchase_request_analytic_account module is installed,
            # add analytic account also to purchase request, not just the lines
            if hasattr(purchase_request_model, 'analytic_account_id'):
                pr_vals['analytic_account_id'] \
                    = self.analytic_account_id and \
                    self.analytic_account_id.id or \
                    False

            pr_res = purchase_request_model.create(pr_vals)

        else:
            pr_res = self.purchase_request_id

        for po_line in purchase_order_line_model.browse(
                self.env.context['active_ids']):
            purchase_request_line_model.create({
                'request_id': pr_res.id,
                'analytic_account_id': self.analytic_account_id and
                self.analytic_account_id.id or False,
                'product_id': po_line.product_id.id,
                'product_uom_id': po_line.product_uom.id,
                'product_qty': po_line.product_qty,
                'name': po_line.name,
            })

        if self.redirect_to_purchase_request:
            return {
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'purchase.request',
                'type': 'ir.actions.act_window',
                'res_id': pr_res.id,
                'context': self.env.context,
            }
        else:
            return {}

    purchase_request_id = fields.Many2one(
        comodel_name='purchase.request',
        string='Purchase Request',
        domain=[('state', 'in', ['draft', 'to_approve'])],
        help='Purchase Requests in Draft or To Approve state'
    )

    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analytic Account',
        help='Analytic Account to be used when creating a new Purchase '
             'Request or adding lines to an existing one'
    )
    type = fields.Selection(
        [('new', 'Create New Purchase Request'),
         ('latest_own', 'Add to Latest own Purchase Request'),
         ('other', 'Add to Other Existing Purchase Request')],
        string='Type',
        required=True,
        default='new',
        help='Choose whether you want to create a new Purchase Request '
             'or add lines to an existing one'
    )
    redirect_to_purchase_request = fields.Boolean(
        string='Show Purchase Request Form',
        default=False
    )
    # Some related fields from selected purchase request account,
    # for quick access to relevant info
    requested_by = fields.Many2one(
        comodel_name='res.users',
        related='purchase_request_id.requested_by',
        string='Requested By',
        readonly=True
    )
    assigned_to = fields.Many2one(
        comodel_name='res.users',
        related='purchase_request_id.assigned_to',
        string='Approver',
        readonly=True
    )
    date_start = fields.Date(
        related='purchase_request_id.date_start',
        string='Creation date',
        readonly=True
    )
    description = fields.Text(
        related='purchase_request_id.description',
        string='Description',
        readonly=True
    )
