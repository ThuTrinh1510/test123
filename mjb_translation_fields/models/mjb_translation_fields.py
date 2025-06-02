from odoo import api, fields, models
from odoo.exceptions import UserError


class MjbTranslationFields(models.Model):
    _name = "x_mjb_translation_fields"
    _description = "Translation Fields"

    x_model_id = fields.Many2one('ir.model', string="Model")
    x_field_id = fields.Many2one('ir.model.fields', string="Field", domain="['&','&',('model_id','=',x_model_id),('translate','=',True),'|',('ttype','=','text'),('ttype','=','char')]")
    x_active = fields.Boolean(string="Active")
    x_lang_ids = fields.Many2many('res.lang', string="Language")

    def confirm_init(self):

        for rec in self:
            init_fields = []
            for lang in rec.x_lang_ids:
                if 'x_studio_' in rec.x_field_id.name:
                    field_checked_x = str(rec.x_field_id.name) + '_' + str(lang.code).lower()
                    field_checked = self.env['ir.model.fields'].search([('model_id','=',rec.x_model_id.model),('name','=',field_checked_x)])
                    init_fields = [field_checked.name]
                else:
                    field_checked_1 = 'x_' + str(rec.x_field_id.name) + '_' + str(lang.code)
                    field_checked_2 = 'x_studio_' + str(rec.x_field_id.name) + '_' + str(lang.code).lower()
                    field_checked = self.env['ir.model.fields'].search([('model_id','=',rec.x_model_id.model),('name','in',[field_checked_1,field_checked_2])])
                    init_fields = [field_checked.name]
                field_records = self.env[rec.x_model_id.model].search([])
                for init_field in init_fields:
                    for record in field_records:
                        self.env.cr.execute('''SELECT %s FROM %s WHERE id = %s''' %(rec.x_field_id.name, record._name.replace('.', '_'), record.id))
                        a=self.env.cr.fetchall()
                        try:
                            init_val = a[0][0][lang.code]
                            self.env.cr.execute('''update %s set "%s"='%s' where id = %s''' %(record._name.replace('.', '_'), init_field, str(init_val).replace("'", '"'), record.id))
                        except Exception as e:
                            init_val = ''
                            self.env.cr.execute('''update %s set "%s"='%s' where id = %s''' %(record._name.replace('.', '_'), init_field, str(init_val).replace("'", '"'), record.id))