from odoo import models

class Lead2OpportunityPartner(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'
    
    def action_apply(self):
        """Inherited core's method to pass the context to create two opportunities from one lead
        """
        if self.name == 'convert': 
            self = self.with_context(opportunity_customization=True)
        return super().action_apply()