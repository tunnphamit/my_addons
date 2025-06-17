
from odoo import fields, models
class Faculty(models.Model):
    _name = 'education_management.faculty'
    _description = 'Faculty Information'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    description = fields.Text(string='Description')

    # Quan hệ 1-n với Khóa
    # program_ids = fields.One2many(
    #     'education_management.program',
    #     'faculty_id',
    #     string='Programs',
    #     help='Programs under this faculty'
    # )

    def __str__(self):
        return self.name