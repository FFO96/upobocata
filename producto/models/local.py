from odoo import models, fields, api

class local(models.Model):
    _name = 'producto.local'
    
    name = fields.Char('Nombre del local', size=64, required=True)
    direccion =  fields.Char("Dirección del local", size=128)
    empleado_ids = fields.One2many("producto.empleado","local_id", "Empleados")
    vehiculo_ids = fields.One2many("producto.vehiculo","local_id", "Empleados")
    pedido_ids = fields.One2many("producto.pedido","local_id", "Pedidos")
    stockingredientes_ids = fields.One2many("producto.stockingredientes","local_id", "Stockingredientes")
    total_empleados=  fields.Integer('Total de empleados del local',compute='_sumatorioEmpleados', store=True)
    
    @api.one
    def _sumatorioEmpleados(self):
        self.total_empleados = 0
        for line in self.empleado_ids:
            self.total_empleados += 1