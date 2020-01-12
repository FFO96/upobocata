# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proveedor(models.Model):
    _name ='producto.proveedor'

    name = fields.Char('nombreEmpresa', size = 64, required=True)
    nif= fields.Char('NIF empresa', size=64)
    direccion = fields.Char('Dirección', size=128)
    ingrediente_ids = fields.One2many("producto.ingrediente","proveedor_id", "Ingredientes")
    total_ingredientes =  fields.Integer('Total de ingredientes del proveedor',compute='_sumatorioIngredientes', store=True)
    
    @api.one
    def _sumatorioIngredientes(self):
        self.total_ingredientes= 0
        for line in self.ingrediente_ids:
            self.total_ingredientes += 1
