# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderLineWizard(models.TransientModel):
    _name = 'purchase.order.line.wizard'

    supplier_id = fields.Many2one(
        "res.partner",
        domain=[('supplier', '=', True)],
    )

    nota = fields.Text(default="Hola")

    order_line_ids = fields.Many2many("purchase.order.line")

    @api.model
    def default_get(self, fields_list):
        res = super(PurchaseOrderLineWizard, self).default_get(fields_list)
        act_ids = self._context.get("active_ids")

        line_ids = self.env['purchase.order.line'].browse(act_ids)
        res.update({
            'order_line_ids': [(6, 0, line_ids.ids)]
        })
        h = ""
        return res

    def create_purchase(self):
        if self.order_line_ids:
            #crea pedido de compra
            order_id = self.env['purchasse.order'].create({
                'partner_id' : self.supplier_id.id
            })

            self.order_line_ids.write({'order_id' : order_id.id})

            action = self.env.ref(purchase.purchase_form_action).read()[0]
            action.update({
                'res_id' : order_id.id
            })
            return action

