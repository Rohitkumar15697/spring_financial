from odoo import models


class Lead2OpportunityPartner(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'
    
    def action_apply(self):
        """Inherited core's method to pass the context to create two opportunities from one lead
        """
        if self.name == 'convert': 
            self = self.with_context(opportunity_customization=True)
            lead_ids = self._context.get('active_ids')
            if len(lead_ids) == 1:
                lead = self.env['crm.lead'].browse(lead_ids[0])
                if lead and not lead.is_lead_complete:
                    return lead.return_completion_wizard()
        return super().action_apply()
