# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountInvoice(models.Model)
    _inherit = ['account.invoice']

    # Campos de idenfificación de la factura.
    secuencial = fields.Integer(string="Secuencial", )
    establecimiento = fields.Integer(string="Establecimiento", )
    puntoemision = fields.Integer(string="Punto de emisión", )

    # Campos de subtotales de la factura.
    basenograiva = fields.Monetary(string="Subtotal no graba I.V.A.", )
    baseimponible = fields.Monetary(string="Subtotal I.V.A. 0%", )
    baseimpgrav = fields.Monetary(string="Subtotal grabado con I.V.A.", )
    baseimpexe = fields.Monetary(string="Subtotal excento de I.V.A.", )
    montoiva = fields.Monetary(string="Monto I.V.A.", )
    montoice = fields.Monetary(string="Monto I.C.E.", )

    # Campos informativos de uso interno.
    total = fields.Monetary(string="TOTAL", )
    subtotal = fields.Monetary(string="SUBTOTAL", )

