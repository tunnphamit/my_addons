# from odoo import models

# class HelpdeskTicket(models.Model):
#     _inherit = 'helpdesk.ticket'

#     def create(self, vals):
#         # Xóa partner_id nếu có, để không gán liên hệ nào
#         vals.pop('partner_id', None)
#         return super().create(vals)
