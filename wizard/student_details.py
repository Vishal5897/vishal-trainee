# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class  StudentDemo(models.TransientModel):
    _name = 'studentdemo.student'
    _description = 'Description'

    name = fields.Char(string='Name')
    fees = fields.Integer(string='Fees')

    def save_action(self):
    	self.env['courece.cource'].create({
    		'courece_name': self.name,
    		'courece_fees': self.fees
    	});
