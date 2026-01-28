from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_cost = fields.Float(
        string="Cost",
        related="product_id.standard_price",
        readonly=True,
        digits="Product Price",
    )
