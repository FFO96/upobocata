from odoo import models, fields, api
from datetime import datetime




class pedido(models.Model):
    _name = 'producto.pedido'
    
    name = fields.Integer('ID pedido: ', size = 10, required=True, default=lambda self: self.env['ir.sequence'].next_by_code('increment_id_pedido'))
    fecha_hora = fields.Datetime(string='Fecha y hora', readonly=True)
    fecha_hora_realizacion = fields.Datetime(string='Fecha y hora de realizacion', readonly=True)
    hora_reparto = fields.Datetime(string='Hora del reparto', readonly=True)
    observaciones = fields.Char('Observaciones del pedido', size=64)
    direccion_envio = fields.Char(string='Dirección de entrega', size=64)
    importe_total =  fields.Float('Importe total del pedido', compute='_sumatorioPrecios')
    en_reparto = fields.Char('En reparto:', default='No', readonly=True)
    
    cliente_id = fields.Many2one("producto.cliente","Cliente")
    nombre_cliente = fields.Char(related="cliente_id.nombre" ,string='Nombre del cliente')
    local_id = fields.Many2one("producto.local","Local")
    empleado_id = fields.Many2one("producto.empleado", "Empleado")
    oferta_id = fields.Many2one("producto.oferta","Oferta aplicada")
    stockbocata_ids = fields.One2many("producto.stockbocata","pedido_id", "stockbocatas")
    
    state = fields.Selection([
        ('crear_pedido', "Pedido creado"),
        ('pedido_realizado', "Pedido realizado"),
        ('pedido_en_reparto', "Pedido en reparto"),
        ('pedido_entregado',"Pedido entregado")
    ], default='crear_pedido')
    
    @api.one
    @api.depends('stockbocata_ids.precio','stockbocata_ids.cantidad','oferta_id.descuento')

    def _sumatorioPrecios(self):
        self.importe_total = 0
        for line in self.stockbocata_ids:
            self.importe_total += line.precio * line.cantidad
        self.importe_total = self.importe_total*(1 - self.oferta_id.descuento)
        
    @api.one
    @api.depends('cliente_id.direccion')
    def action_client(self):
        self.direccion_envio = self.cliente_id.direccion

    @api.multi
    def action_create(self):
        self.state = 'pedido_realizado'
        self.fecha_hora = datetime.today()

    @api.multi
    def action_realized(self):
        self.state = 'pedido_en_reparto'
        self.en_reparto = 'Puede ser repartido'
        self.fecha_hora_realizacion = datetime.today()

    @api.multi
    def action_deliver(self):
        self.state = 'pedido_entregado'
        self.en_reparto = 'Si'
        
    @api.multi
    def action_delivered(self):
        self.state = 'pedido_entregado'
        self.en_reparto = 'Entregado'
        self.hora_reparto = datetime.today()
        
    
        
        
            