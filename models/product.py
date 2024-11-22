# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    sale_delay = fields.Integer(company_dependent=True)


    # -*- coding: utf-8 -*-
class Product(models.Model):
    _inherit = 'product.product'
    sale_delay = fields.Integer(company_dependent=True)