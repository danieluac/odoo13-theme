# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class theme_loengo(models.Model):
#     _name = 'theme_loengo.theme_loengo'
#     _description = 'theme_loengo.theme_loengo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
