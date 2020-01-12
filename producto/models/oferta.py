# -*- coding: utf-8 -*-

from odoo import models, fields, api

class oferta(models.Model):
    _name ='producto.oferta'
    
    name = fields.Integer('ID de la oferta', size = 10, required=True, default=lambda self: self.env['ir.sequence'].next_by_code('increment_id_ingrediente'))
    nombre = fields.Char('Nombre de la oferta', size=64, required=True)
    descuento = fields.Float('Descuento de la oferta', size=128, required=True)
    
    pedido_ids = fields.One2many("producto.pedido","oferta_id", "Pedidos")