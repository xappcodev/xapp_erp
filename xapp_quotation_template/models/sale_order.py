# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class SaleOrderPaymentPlan(models.Model):
    _name = 'sale.order.payment.plan'
    _description = 'Sale Order Payment Plan'
    _order = 'sequence, id'

    sequence = fields.Integer(string='Sequence', default=10)
    order_id = fields.Many2one('sale.order', string='Order Reference', required=True, ondelete='cascade', index=True)
    name = fields.Char(string='Payment Stage', required=True)
    description = fields.Char(string='Description')
    percentage = fields.Float(string='Percentage (%)', required=True, default=0.0)
    amount = fields.Monetary(string='Amount', compute='_compute_amount', store=True)
    currency_id = fields.Many2one(related='order_id.currency_id', depends=['order_id.currency_id'], store=True)

    @api.depends('percentage', 'order_id.amount_total')
    def _compute_amount(self):
        for plan in self:
            plan.amount = (plan.percentage / 100.0) * plan.order_id.amount_total


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    xapp_development_type = fields.Selection([
        ('Software', 'Software'),
        ('Web', 'Web'),
        ('Mobile', 'Mobile'),
        ('IT', 'IT'),
        ('Other', 'Other')
    ], string='Development')
    xapp_quotation_terms = fields.Html(
        string='Quotation Terms',
        default=lambda self: self.env.company.xapp_quotation_terms
    )
    xapp_payment_plan_ids = fields.One2many('sale.order.payment.plan', 'order_id', string='Payment Plans')

    @api.constrains('xapp_payment_plan_ids')
    def _check_payment_plan_percentage(self):
        for order in self:
            if order.xapp_payment_plan_ids:
                total_percentage = sum(order.xapp_payment_plan_ids.mapped('percentage'))
                if round(total_percentage, 2) != 100.0:
                    raise ValidationError("The total percentage of the payment plan must be exactly 100%.")
