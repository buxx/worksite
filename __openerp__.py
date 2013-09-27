# -*- coding: utf-8 -*-
{
    'name': 'Worksite',
    'version': '0.0.1',
    'category': 'Project',
    'sequence': 3,
    'author': 'Bastien Sevajol',
    'summary': 'Manage worksites',
    'description': """
Manage worksites
======================================

DESCRIPTION
    """,
    'depends': [
        'product',
        'stock'
    ],
    'data': [
        'worksite_view.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}