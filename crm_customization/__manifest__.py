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
    'version': '1.0.0',
    'application': True,
    'sequence': 1,
}