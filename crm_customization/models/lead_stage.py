from odoo import models, fields

class LeadStages(models.Model):
    _name = "crm.lead.stage"
    _description = "Lead Stages Model"
    
    name = fields.Char('name')