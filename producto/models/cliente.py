# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cliente(models.Model):
    _name = 'producto.cliente'
    
    
    name = fields.Integer('ID cliente', size = 10, required=True, default=lambda self: self.env['ir.sequence'].next_by_code('increment_id_cliente'))
    dni = fields.Char('DNI cliente', size = 64, required=True)
    nombre = fields.Char('Nombre del cliente', size=64, required=True)
    telefono =  fields.Integer("Teléfono del cliente", size=128) 
    email = fields.Char("Email del cliente")
    direccion = fields.Char("Dirección habitual del cliente")
    pedido_ids = fields.One2many("producto.pedido","cliente_id", "Pedidos")
    
    