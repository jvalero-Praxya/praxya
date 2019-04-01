 #-*- coding: utf-8 -*-

from odoo import api, models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tipology = fields.Selection(
        selection=[
            ['metal', 'Metal'],
            ['pvc', 'Pvc'],
            ['cristal', 'Cristal']
        ]
    )