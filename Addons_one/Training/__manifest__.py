{
    'name': 'Training',
    'version': '1.0',
    'category': 'Training',
    'summary': 'Training Management System',

    'depends': [
        'base',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/training_views.xml',
        'views/menu.xml',
    ],

    'installable': True,
    'application': True,
}