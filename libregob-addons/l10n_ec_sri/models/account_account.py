# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountTax(models.Model):
    _inherit = 'account.tax'
    _order = 'sequence asc'

    sustento_id = fields.Many2one(
            'l10n_ec_sri.sustento', ondelete='restrict',
            string="Sustento tributario", )
