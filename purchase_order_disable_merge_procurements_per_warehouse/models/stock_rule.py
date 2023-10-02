from odoo import api, models


class StockRule(models.Model):

    _inherit = "stock.rule"

    @api.model
    def _merge_procurements(self, procurements_to_merge):
        """A modification to disable merging procurements based on warehouse's
        never_merge_procurements -field."""
        merged_procurements = super()._merge_procurements(procurements_to_merge)

        procurements = []
        warehouse = []

        for procurement in procurements_to_merge:
            # Do not include False values just in case and
            # check if proc is a list
            if procurement and isinstance(procurement, list):
                # procurement can have several items, so we loop it
                for proc in procurement:
                    procurements.append(proc)
                    if proc.values.get("warehouse_id") not in warehouse:
                        warehouse.append(proc.values.get("warehouse_id"))
        # See if there are procurements from more than one warehouse.
        # Then check if that warehouse has merging procurements disabled.
        if len(warehouse) == 1 and warehouse[0].never_merge_procurements:
            return procurements
        else:
            return merged_procurements
