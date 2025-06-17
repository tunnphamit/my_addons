
from odoo import fields, models
class Program(models.Model):
    _name = 'education_management.faculty'
    _description = 'Faculty Information'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

    # # Relationship with students
    # student_ids = fields.One2many(
    #     'education_management.student',
    #     'faculty_id',
    #     string='Students',
    #     help='List of students in this faculty'
    # )

    def __str__(self):
        return self.name