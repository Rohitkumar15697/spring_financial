{
    'name': 'CRM Customization',
    'summary': """
        Customization for CRM module. Creating two different types
        of opportunities from one lead
    """,
    'depends':['crm'],
    'data':[
        'views/crm_lead_view.xml',
            ],
    'assets': {
        'web.assets_backend': [
            'crm_customization/static/src/core/*/**',
        ]
    },
    'version': '1.0.0',
    'license': 'LGPL-3',
    'application': True,
    'sequence': 1,
}