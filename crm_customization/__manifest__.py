{
    'name': 'CRM Customization',
    'summary': """
        Customization for CRM module. Creating two different types
        of opportunities from one lead
    """,
    'depends':['crm'],
    'data':[
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/crm_lead_view.xml',
        'wizard/lead_completion_wizard.xml',
            ],
    'assets': {
        'web.assets_backend': [
            'crm_customization/static/src/*/**',
        ],
        'web.assets_frontend': [
            'crm_customization/static/src/*/**',
        ],
    },
    'version': '1.0.0',
    'license': 'LGPL-3',
    'application': True,
    'sequence': 1,
}
