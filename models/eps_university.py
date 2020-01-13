# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime
from odoo import fields, models, api


class University(models.Model):
    _name = 'university.university'
    _description = 'university Description'
    _rec_name = "university_name"

    university_name = fields.Char(string="University Name")
    university_address = fields.Char(string='University Address')
    university_contact = fields.Integer(string='Number')


class Institute(models.Model):
    _name = 'institute.institute.details'
    _description = 'institute details'
    _rec_name = "institute_name"

    institute_name = fields.Char(string='Institute Name')
    institute_university_name = fields.Many2one(
        'university.university', string='University Name')
    # institute_cource = fields.One2many('courece.cource','courece_institutes',string='Cource Name')

    @api.model
    def create(self,vals):
        print("\n\n\n\n")
        print(">>>>>>>>>>>>>> in create method")
        print(">>>>>>>>>>>>>>>>>>>>>.values", vals)
        return super(Institute, self).create(vals)


    def write(self, vals):
        print("\n\n\n\n")
        print(">>>>>>>>>>>>>> in write method")
        print(">>>>>>>>>>>>>>>>>>>>>.values", vals)
        return super(Institute, self).write(vals)

    def unlink(self):
        print("\n\n\n\n")
        print(">>>>>>>>>>>>>> in unlink method", self)
        return super(Institute, self).unlink()


class Cource(models.Model):
    _name = 'courece.cource'
    _description = 'Description'
    _rec_name = "courece_name"

    courece_name = fields.Text(string='Cource Name')
    courece_fees = fields.Integer(string='courece fees')
    # courece_institutes = fields.Many2one("institute.institute.details")
    # students_cources = fields.Many2one('student.student',string='Field Label')


class Student(models.Model):
    _name = 'student.student'
    _description = 'Description'
    _rec_name = "total_leave"

    student_roll_no = fields.Integer(string='Roll Number')
    student_mail_id = fields.Char(string="Mail id")
    student_institute = fields.Many2one(
        'institute.institute.details', string='Institute Name')
    student_cource = fields.Many2one('courece.cource', string='Cource Name')
    state = fields.Selection([('draft', 'New'), ('confirm', 'confirm'), ('done', 'done')], default='draft')
    student_leave_date = fields.Date(string='Start date to leave', default=datetime.today(),store=True)
    student_leave_date_end = fields.Date(string='end` date to leave',store=True)
    total_leave = fields.Integer(string="Total Leave", compute="_compute_total")

    _sql_constraints = [
        ('student_roll_no', 'unique(student_roll_no)',
         'Can t be duplicate value for this field! student no')
    ]


    def draft(self):
        for rec in self:
            rec.write({'state': 'draft'})

    def confirm(self):
        for rec in self:
            rec.write({'state':'confirm'})

    def done(self):
        for rec in self:
            rec.write({'state':'done'})

    def _compute_total(self):
        for i in self:
            if i.student_leave_date and i.student_leave_date_end:
                diff = i.student_leave_date_end - i.student_leave_date
                i.total_leave = diff.days
            else:
                i.total_leave = 2

    # @api.model
    # def get_all_data(self):
    #     return self.search([])