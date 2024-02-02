# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sge2024(models.Model):
#     _name = 'sge2024.sge2024'
#     _description = 'sge2024.sge2024'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
