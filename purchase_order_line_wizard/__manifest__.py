# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Line wizard",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Modulo creado po Jaime
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/o
    # doo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        #'views/product_view.xml',
        'wizard/purchase_order_line_wizard_view.xml',
    ],
    'installable': True,
    'application': True,

}
