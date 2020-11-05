# -*- coding: utf-8 -*-
# from odoo import http


# class ThemeLoengo(http.Controller):
#     @http.route('/theme_loengo/theme_loengo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_loengo/theme_loengo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_loengo.listing', {
#             'root': '/theme_loengo/theme_loengo',
#             'objects': http.request.env['theme_loengo.theme_loengo'].search([]),
#         })

#     @http.route('/theme_loengo/theme_loengo/objects/<model("theme_loengo.theme_loengo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_loengo.object', {
#             'object': obj
#         })
