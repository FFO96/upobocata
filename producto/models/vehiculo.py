
from odoo import models, fields, api
from Crypto.Util.number import size
from wtforms.validators import required
from _datetime import timedelta

class vehiculo(models.Model):
    _name = 'producto.vehiculo'
    
    name = fields.Integer('ID vehículo', size = 10, required=True, default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    matricula = fields.Char('Matrícula del vehículo', size = 10, required=True)
    fechaAlta = fields.Date('Fecha de alta', required = True)
    fechaRevision = fields.Date('Fecha de revisión')
    modelo =  fields.Char("Modelo del vehículo", size=64)
    local_id = fields.Many2one("producto.local","Local")
    empleado_ids = fields.Many2many("producto.empleado",string="Empleados conductores")

    