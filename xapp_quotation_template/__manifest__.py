# -*- coding: utf-8 -*-
{
    'name': 'Xapp Professional Quotation Template',
    'version': '18.0.1.1.0',
    'category': 'Sales/Sales',
    'summary': 'Custom Quotation Report with Payment Plans & Terms',
    'description': """
Xapp Professional Quotation Template
====================================
Provides a standalone custom quotation report matching Xapp branding and requirements.
Includes a dynamic Payment Plan model and customizable Terms & Conditions.
    """,
    'author': 'Xapp Softwares & Web Solutions',
    'website': 'https://www.xapp.com',
    'depends': ['sale_management', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'data/company_data.xml',
        'views/res_config_settings_views.xml',
        'views/sale_order_views.xml',
        'reports/quotation_report_action.xml',
        'reports/quotation_report_template.xml',
    ],
    'demo': [
        'demo/sale_order_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
