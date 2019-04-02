 #-*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.exceptions import ValidationError


class LibraryBook(models.Model):
    _name = "library.book"

    name= fields.Char(string="Book")

    description = fields.Text(string="Description")

    isbn = fields.Char("ISBN")


    category_id = fields.Many2one(

        comodel_name="library.category",
        inverse_name="book_id",
        string="Categorias")

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'El nombre del libro no puede repetirse',)
    ]

    categ_count = fields.Integer(
        string="Nº de Categorias",
        compute="_count_categ"
    )

    def _count_categ(self):
        for book in self:
            book.categ_count = len(book.category_id)

    @api.constrains("isbn")
    def check_isbn(self):
        isbn = self.search([['id', '!=', self.id]]).mapped("isbn")
        if self.isbn and self.isbn in isbn:
            raise ValidationError(_('ISBN Duplicado'))
