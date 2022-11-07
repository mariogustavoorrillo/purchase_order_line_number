from odoo import tools, models, fields, api, _
from datetime import datetime

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def _compute_purchase_order_line_number(self):
        for rec in self:
            res = 0
            res = len(self.env['purchase.order.line'].search([('order_id','=',rec.order_id.id),('id','<',rec.id)])) 
            rec.purchase_order_line_number = res + 1

    purchase_order_line_number = fields.Integer('Number',compute=_compute_purchase_order_line_number)
