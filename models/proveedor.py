# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proveedor(models.Model):
    _name ='producto.proveedor'

    name = fields.Char('nombreEmpresa', size = 64, required=True)
    nif= fields.Char('NIF empresa', size=64)
    direccion = fields.Char('Dirección', size=128)
    ingrediente_ids = fields.One2many("producto.ingrediente","proveedor_id", "Ingredientes")
