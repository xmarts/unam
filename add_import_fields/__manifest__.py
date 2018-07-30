# -*- coding: utf-8 -*-
{
    'name': "Add Import Fields",

    'summary': """
        Add fields to budget lines""",

    'description': """
        Add fields amount exercised and amount committed to budget lines
    """,

    'author': "Xmarts",
    'website': "http://xmarts.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','account_budget'],

    'data': [
        'views/views.xml',
    ]
}