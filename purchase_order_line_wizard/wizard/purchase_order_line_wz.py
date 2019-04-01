 #-*- coding: utf-8 -*-

from odoo import models, fields

class PurchaseOrderLineWizard(models.TransientModel):
    _name = 'purchase.order.line.wizard'

    supplier_id = fields.Many2one(
        "res.partner",
        domain=[('supplier', '=', True)],
    )

    order_line_ids= fields.Many2many("purchase.order.line")