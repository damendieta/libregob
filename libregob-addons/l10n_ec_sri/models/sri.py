# -*- coding: utf-8 -*-
from odoo import models, fields


class SriSustento(models.Model):
    _name = 'l10n_ec_sri.sustento'
    """
    En este campo obligatorio se debe indicar si el comprobante ingresado
    sustenta crédito  tributario  o  sustenta  costos  o  gastos,  el  campo
    es  de  dos  caracteres, según las especificaciones de la Tabla 5. 
    """
    name = fields.Char(string="Sustento tributario", )
    code = fields.Char(string="Code", )
    codigo_tipo_comprobante = fields.Char(string="Comprobantes permitidos", )
    description = fields.Char(string="Description", )
    fecha_inicio = fields.Date(string="Fecha de inicio", )
    fecha_fin = fields.Date(string="Fecha de fin", )


class SriComprobante(models.Model):
    _name = 'l10n_ec_sri.comprobante'
    """
    Corresponde  al  tipo  de  comprobante  utilizado  en  la  transacción
    que  se  va  a registrar según lo indicado en la Tabla 4.
    """
    name = fields.Char(string="Comprobante", )
    code = fields.Char(string="Code", )
    sequence = fields.Integer(string="Sequence", )

