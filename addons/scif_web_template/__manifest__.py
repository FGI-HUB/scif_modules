# -*- coding: utf-8 -*-
{
    'name': "Scif Immobilier Web Template",

    'summary': """Web public template for Odoo 12""",

    'description': """
        Template de site web immobilier.
    """,

    'author': "EWONGA Sarl",
    'website': "https://www.ewonga.tech",

    'category': 'Theme/Creative',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/navbar.xml',
        'views/footer.xml',
        'views/assets.xml',
        'views/assets_js.xml',
        #'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}