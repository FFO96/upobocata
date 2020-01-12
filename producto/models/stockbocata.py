from odoo import models, fields


class stockbocata(models.Model):
    _name = 'producto.stockbocata'

    name = fields.Integer('ID stockbocata', size = 10, required=True, default=lambda self: self.env['ir.sequence'].next_by_code('increment_id_stockbocata'))
    #bocata_id = fields.Many2one("producto.bocata","Bocata")
    bocata_id = fields.Many2many("producto.bocata",string="Bocata en pedido")
    nombre = fields.Char(related='bocata_id.nombre', string='Nombre')
    precio = fields.Float(related='bocata_id.precio', string='Precio')
    cantidad = fields.Integer('Número de bocatas', size = 10, required=True)

    pedido_id = fields.Many2one("producto.pedido","Pedido")