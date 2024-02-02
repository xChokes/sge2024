# -*- coding: utf-8 -*-
# from odoo import http


# class Sge2024(http.Controller):
#     @http.route('/sge2024/sge2024', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sge2024/sge2024/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sge2024.listing', {
#             'root': '/sge2024/sge2024',
#             'objects': http.request.env['sge2024.sge2024'].search([]),
#         })

#     @http.route('/sge2024/sge2024/objects/<model("sge2024.sge2024"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sge2024.object', {
#             'object': obj
#         })
