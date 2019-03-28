# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryCategory(models.Model):
    _name="library.category"

    name= fields.Char(string="Category")
    description= fields.Text(string="Description")

