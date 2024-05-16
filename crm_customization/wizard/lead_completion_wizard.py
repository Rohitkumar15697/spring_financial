from odoo import models

from logging import getLogger
_logger = getLogger(__name__)

class LeadCompletion(models.TransientModel):
    _name = "lead.complete.wizard"
    _description = "Lead Completion Wizard"
    
    def lead_mark_as_complete(self):
        """Wizard button 'Mark as complete' to the lead when we select one lead to 
        convert to opportunity
        """
        _logger.info(self._context)
        active_lead_id = self._context.get('active_lead_id')
        if active_lead_id:
            lead = self.env['crm.lead'].browse(int(active_lead_id))
            lead.mark_lead_as_complete()