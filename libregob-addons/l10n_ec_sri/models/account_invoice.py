# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountInvoice(models.Model)
    _inherit = ['account.invoice']

    secuencial = fields.Integer(string="Secuencial", )
    establecimiento = fields.Integer(string="Establecimiento", )
    puntoemision = fields.Integer(string="Punto de emisión", )
