# -*- coding: utf-8 -*-
from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    xapp_quotation_terms = fields.Html(string="Quotation Terms & Conditions", translate=True)
