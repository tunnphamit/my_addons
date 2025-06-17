
from odoo import models, fields

class Student(models.Model):
    _name = 'education.student'
    _description = 'Student Information'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Student name', required=True)
    dob = fields.Date(string='Date of Birth', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone', required=True)
    address = fields.Text(string='Address', required=True)
    avatar = fields.Binary(string='Avatar', help='Ảnh đại diện')

    active = fields.Boolean('Active', default=True)

    # # Khoa
    # faculty = fields.Many2one(
    #     'education_management.faculty',
    #     string='Faculty',
    #     help='Sinh viên thuộc khoa nào',
    #     required=True
    # )

    # # Khóa
    # program = fields.Many2one(
    #     'education_management.program',
    #     string='Program',
    #     help='Sinh viên thuộc khóa nào',
    #     required=True
    # )

    # # Ngành
    # major = fields.Many2one(
    #     'education_management.major',
    #     string='Major',
    #     help='Sinh viên thuộc ngành nào',
    #     required=True
    # )



    def __str__(self):
        return self.name