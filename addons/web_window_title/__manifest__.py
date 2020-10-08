# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': "Web Window Title",
    'summary': "The custom web window title",
    'author': "EWONGA SARL",
    'website': "https://ewonga.tech",
    'support': 'odoo@ewonga.tech',
    'category': 'Extra Tools',
    'version': '1.1',
    'depends': ['base_setup'],
    'demo': [
        'data/demo.xml',
    ],
    'data': [
        'views/webclient_templates.xml',
        'views/res_config.xml',
    ],
    'images': [
        'static/description/main_screenshot.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}