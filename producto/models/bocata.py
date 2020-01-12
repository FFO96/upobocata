# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bocata(models.Model):
    _name = 'producto.bocata'
    
    name = fields.Integer('ID bocata', size = 10, required=True, default=lambda self: self.env['ir.sequence'].next_by_code('increment_id_bocata'))
    nombre = fields.Char('Nombre del bocata', size=64, required=True)
    elaboracion =  fields.Char("Elaboración del bocata", size=128) 
    precio = fields.Float("Precio del bocata", required=True)
    ingrediente_ids = fields.Many2many("producto.ingrediente",string="Ingredientes del bocata")
    stockbocata_ids = fields.Many2many("producto.stockbocata",string="Stock del bocata")
    
    
    @api.constrains('precio', 'nombre')
    def _check_precio(self):
        for bocata in self: 
            if bocata.precio < 1.99:
                return False
        return True

    _constraints = [
        (_check_precio, 'Como minimo debe valer 2€', ['precio'])
    ]

    _sql_constraints = [('nombre_unique','UNIQUE(nombre)',"El nombre no puede repetirse"),]