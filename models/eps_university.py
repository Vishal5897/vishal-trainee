# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


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
    institute_university_name = fields.Many2one('university.university',string='University Name')
    institute_cource = fields.One2many('courece.cource','courece_institutes',string='Cource Name')

class Cource(models.Model):
    _name = 'courece.cource'
    _description = 'Description'
    _rec_name = "courece_name"

    courece_name = fields.Text(string='Cource Name') 
    courece_fees = fields.Integer(string='courece fees')
    courece_institutes = fields.Many2one("institute.institute.details")
    # students_cources = fields.Many2one('student.student',string='Field Label') 

class Student(models.Model):
    _name = 'student.student'
    _description = 'Description'

    student_roll_no = fields.Integer(string='Roll Number')
    student_mail_id = fields.Char(string="Mail id")
    student_cource = fields.Many2one('courece.cource',string='Field Label')


    _sql_constraints = [
('student_roll_no', 'unique(student_roll_no)', 'Can t be duplicate value for this field!')
]