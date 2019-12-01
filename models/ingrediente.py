# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ingrediente(models.Model):
    _name ='producto.ingrediente'
    
    name = fields.Integer('ID ingrediente', size = 10, required=True)
    nombre = fields.Char('Nombre del ingrediente', size=64, required=True)
    cantidad = fields.Integer('Cantidad del ingrediente', required=True)
    caducidad = fields.Date('Fecha de caducidad',required=True)
    bocata_ids = fields.Many2many("producto.bocata",string="Bocatas con el ingrediente")
    proveedor_id = fields.Many2one("producto.proveedor","Proveedor")