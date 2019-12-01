# -*- coding: utf-8 -*-
from odoo import http

# class Producto(http.Controller):
#     @http.route('/producto/producto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/producto/producto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('producto.listing', {
#             'root': '/producto/producto',
#             'objects': http.request.env['producto.producto'].search([]),
#         })

#     @http.route('/producto/producto/objects/<model("producto.producto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('producto.object', {
#             'object': obj
#         })