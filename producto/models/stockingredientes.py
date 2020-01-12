from odoo import models, fields, api


class stockingredientes(models.Model):
    _name = 'producto.stockingredientes'
    
    name = fields.Integer('ID stockingredientes', size = 10, required=True, default=lambda self: self.env['ir.sequence'].next_by_code('increment_id_stockingredientes'))
    ingrediente_id = fields.Many2many("producto.ingrediente",string="Ingrediente en stock")
    nombre = fields.Char(related='ingrediente_id.nombre', string='Nombre')
    caducidad = fields.Date('Caducidad',required=True)
    cantidad = fields.Integer('Número de ingredientes', size = 10, required=True)
    
    local_id = fields.Many2one("producto.local","Local")