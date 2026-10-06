{
    'name': 'Sales Pricing Report',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Adds a Pricing report in Sales module with Website Development Costs.',
    'description': 'This module adds a new Pricing report to the Sales Order that includes website development costs referenced from Aero Business Solutions.',
    'depends': ['sale', 'sale_management'],
    'data': [
        'reports/pricing_report_action.xml',
        'reports/pricing_report_template.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
