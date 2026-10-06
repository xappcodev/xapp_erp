# -*- coding: utf-8 -*-
from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    xapp_quotation_terms = fields.Html(
        related='company_id.xapp_quotation_terms', 
        string="Quotation Terms & Conditions", 
        readonly=False
    )
