
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('email', 'phone')
    def _check_unique_email_phone(self):
        for partner in self:
            # Kiểm tra trùng email
            if partner.email:
                duplicate_email = self.search([
                    ('email', '=', partner.email),
                    ('id', '!=', partner.id)
                ], limit=1)
                if duplicate_email:
                    raise ValidationError(_('Đã tồn tại Liên hệ có Email "%s" trên hệ thống. Vui lòng kiểm tra lại!') % partner.email)

            # Kiểm tra trùng số điện thoại
            if partner.phone:
                duplicate_phone = self.search([
                    ('phone', '=', partner.phone),
                    ('id', '!=', partner.id)
                ], limit=1)
                if duplicate_phone:
                    raise ValidationError(_('Đã tồn tại Liên hệ có Số điện thoại "%s" trên hệ thống. Vui lòng kiểm tra lại!') % partner.phone)