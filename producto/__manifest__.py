# -*- coding: utf-8 -*-
{
    'name': "producto",
    'summary': """Gestión del producto""",
    'description': """Gestion del producto:bocatas, ingredientes, local...""",
    'author': "Grupo 2 - TSI",
    'category': 'producto',
    'version': '0.1',
    'depends': ['base'],
    'data': ['views/bocata_view.xml', 'views/ingrediente_view.xml','views/proveedor_view.xml','views/local_view.xml',
             'views/empleado_view.xml','views/vehiculo_view.xml','views/pedido_view.xml','views/cliente_view.xml','views/oferta_view.xml',
              'views/stockingredientes_view.xml','views/stockbocata_view.xml'],
    'demo': ['demo/producto_demo.xml'],
    'application': True,
}