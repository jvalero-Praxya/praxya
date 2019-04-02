# -*- coding: utf-8 -*-
{
    'name': "Report Jaime",

    'summary': """
        Reporte de ejemplo""",

    'description': """
        Report
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/o
    # doo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'report/account_invoice_report.xml',
        'report/report.xml',
        'report/templates.xml',
    ],
    'installable': True,

}
