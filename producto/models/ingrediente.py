# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ingrediente(models.Model):
    _name ='producto.ingrediente'
    
    name = fields.Integer('ID ingrediente', size = 10, required=True, default=lambda self: self.env['ir.sequence'].next_by_code('increment_id_ingrediente'))
    nombre = fields.Char('Nombre del ingrediente', size=64, required=True)
    bocata_ids = fields.Many2many("producto.bocata",string="Bocatas con el ingrediente")
    proveedor_id = fields.Many2one("producto.proveedor","Proveedor")
    stockingrediente_id = fields.Many2many("producto.stockingredientes",string="Stock del ingrediente")
    total_bocatas =  fields.Integer('Total de bocatas con el ingrediente',compute='_sumatorioBocatas', store=True)
    
    @api.one
    def _sumatorioBocatas(self):
        self.total_bocatas = 0
        for line in self.bocata_ids:
            self.total_bocatas += 1
