# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = ['account.invoice']

    # Campos de idenfificación de la factura.
    secuencial = fields.Integer(string="Secuencial", )
    establecimiento = fields.Integer(string="Establecimiento", )
    puntoemision = fields.Integer(string="Punto de emisión", )
    autorizacion = fields.Char(string="Autorizacion", )

    # Campos de subtotales de la factura.
    basenograiva = fields.Monetary(
            string="Subtotal no graba I.V.A.", readonly=True, )
    baseimponible = fields.Monetary(
            string="Subtotal I.V.A. 0%", readonly=True, )
    baseimpgrav = fields.Monetary(
            string="Subtotal grabado con I.V.A.", readonly=True, )
    baseimpexe = fields.Monetary(
            string="Subtotal excento de I.V.A.", readonly=True, )
    montoiva = fields.Monetary(
            string="Monto I.V.A.", readonly=True, )
    montoice = fields.Monetary(
            string="Monto I.C.E.", readonly=True, )

    # Campos informativos de uso interno.
    total = fields.Monetary(
            string="TOTAL", readonly=True, )
    subtotal = fields.Monetary(
            string="SUBTOTAL", readonly=True, )

    @api.onchange('invoice_line_ids')
    def _onchange_invoice_line_ids(self):
        """
        Necesario para calcular los impuestos según el formato de Ecuador.
        """
        tax_lines = self.tax_line_ids
        self.basenograiva = sum(tax_lines.filtered(
            lambda: l.tax_id.tax_group_id.name == "NoGraIva").mapped('base'))

        self.baseimponible = sum(tax_lines.filtered(
            lambda: l.tax_id.tax_group_id.name == "Imponible").mapped('base'))

        self.baseimpgrav = sum(tax_lines.filtered(
            lambda: l.tax_id.tax_group_id.name == "ImpGrav").mapped('base'))

        self.baseimpexe = sum(tax_lines.filtered(
            lambda: l.tax_id.tax_group_id.name == "ImpExe").mapped('base'))

        self.montoiva = sum(tax_lines.filtered(
            lambda: l.tax_id.tax_group_id.name == "Imponible").mapped('amount_total'))

        self.montoice = sum(tax_lines.filtered(
            lambda: l.tax_id.tax_group_id.name == "Ice").mapped('amount_total'))

        return super(AccountInvoice, self)._onchange_invoice_line_ids()

