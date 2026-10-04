from odoo import models, fields

class Training(models.Model):
    _name = 'training.training'
    _description = 'Training'

    name = fields.Char(
        string='Training Name',
        required=True
    )

    trainer = fields.Char(
        string='Trainer'
    )

    date = fields.Date(
        string='Training Date'
    )

    duration = fields.Float(
        string='Duration'
    )
    description = fields.Text(
        string='Description'
    )