# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryBook(models.Model):
    _name="library.book"

    name= fields.Char(string="Book")
    description= fields.Text(string="Description")

    category_id = fields.Many2one(

        comodel_name="library.category", string="Categoria")