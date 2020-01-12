from odoo import models, fields, api

class local(models.Model):
    _name = 'producto.local'
    
    name = fields.Char('Nombre del local', size=64, required=True)
    direccion =  fields.Char("Dirección del local", size=128)
    #ingrediente_ids = fields.Many2many("producto.ingrediente",string="Ingredientes del bocata")
    empleado_ids = fields.One2many("producto.empleado","local_id", "Empleados")
    vehiculo_ids = fields.One2many("producto.vehiculo","local_id", "Empleados")
    pedido_ids = fields.One2many("producto.pedido","local_id", "Pedidos")
    stockingredientes_ids = fields.One2many("producto.stockingredientes","local_id", "Stockingredientes")