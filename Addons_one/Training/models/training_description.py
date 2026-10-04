from odoo import fields, models
class TrainingDescription(models.Model):
    _name = 'training.description'
    _description = 'New Model Description'
    _order = 'id desc'

    description = fields.Char(string='Description', required=True)