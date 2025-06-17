# -*- coding: utf-8 -*-

{
    'name' : 'Education Management',
    'version' : '1.0',
    'summary': '',
    'sequence': 10,
    'description': 'Quản lý đào tạo',
    'category': 'Accounting/Accounting',
    'depends': [
        'base',
        'web',
        'mail',
        'calendar',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',

        # menus
        'views/education_management_menus.xml',
    ],
    
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
