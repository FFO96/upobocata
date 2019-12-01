# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bocata(models.Model):
    _name = 'producto.bocata'
    
    name = fields.Integer('ID bocata', size = 10, required=True)
    nombre = fields.Char('Nombre del bocata', size=64, required=True)
    elaboracion =  fields.Char("Elaboración del bocata", size=128) 
    precio = fields.Float("Precio del bocata")
    ingrediente_ids = fields.Many2many("producto.ingrediente",string="Ingredientes del bocata")