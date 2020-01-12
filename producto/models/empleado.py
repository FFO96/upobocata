
from odoo import models, fields, api
from Crypto.Util.number import size

class empleado(models.Model):
    _name = 'producto.empleado'
    
    name = fields.Integer('ID empleado', size = 10, required=True, default=lambda self: self.env['ir.sequence'].next_by_code('increment_id_empleado'))
    dni = fields.Char('DNI del empleado', size = 10, required=True)
    nombre = fields.Char('Nombre del empleado', size=64, required=True)
    telefono = fields.Integer('Telefono del empleado', size=64)
    direccion =  fields.Char("Direccion del empleado", size=128) 
    puesto =  fields.Char("Puesto del empleado", size=128) 
    local_id = fields.Many2one("producto.local","Local")
    vehiculo_ids = fields.Many2many("producto.vehiculo",string="Vehículos para conducir")
    
    @api.constrains('nombre', 'dni')
    def _check_name(self):
        for empleado in self: 
            if len(empleado.nombre) < 4:
                return False
        return True

    _constraints = [
        (_check_name, 'nombre debe tener almenos 4 caracteres.', ['nombre'])
    ]

    _sql_constraints = [('dni_unique','UNIQUE(dni)',"El dni no puede repetirse"),]
    
    @api.onchange('vehiculo_ids','puesto')
    def _cambiar_puesto(self):
        if self.vehiculo_ids.name!='':
            self.puesto='Repartidor'
        else:
            self.puesto=''