# -*- coding: utf-8 -*-
{
    'name': "Custom Web Module",

    'summary': """Web public template for Odoo""",

    'description': """
        Override basic HTML Web module then set a customizable external module
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
        'views/templates.xml',
        'views/template_about.xml',
        'views/template_contact.xml',
        'views/template_home.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}