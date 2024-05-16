from odoo import models, fields
from odoo.exceptions import UserError

class Lead(models.Model):
    _inherit = "crm.lead"

    opportunity_type = fields.Selection([
        ('technology', 'Technology'),
        ('business', 'Business'),
    ], string="Opportunity Type")
    
    lead_stages = fields.Selection([
        ('new', 'NEW'),
        ('under_review', 'Under Review'),
        ('complete', 'Complete'),
    ], default="new") # We can also create Many2one field for the states
    

    def convert_opportunity(self, partner, user_ids=False, team_id=False):
        """Override complete method to get the required customization flow
        """
        if not self._context.get('opportunity_customization'):
            return super().convert_opportunity(partner, user_ids, team_id)

        # Create extra opportunity of opportunity type 'technology'
        customer = partner if partner else self.env['res.partner']
        for lead in self:
            if lead.lead_stages =='complete':
                if not lead.active or lead.probability == 100:
                    continue
                vals = lead._convert_opportunity_data(customer, team_id)
                lead.write(vals)
                
                tech_lead = lead.sudo().copy()
                vals = tech_lead.with_context(technical_opportunity=True)._convert_opportunity_data(customer, team_id)
                tech_lead.write(vals)
            else:
                raise UserError('Leads can not be converted into Opportunity if it is not in Complete State!')
            # =====================================================
            
        if user_ids or team_id:
            self._handle_salesmen_assignment(user_ids=user_ids, team_id=team_id)
        return True

    def _convert_opportunity_data(self, customer, team_id=False):
        upd_values = super()._convert_opportunity_data(customer, team_id)
        if self._context.get('opportunity_customization'):
            if self._context.get('technical_opportunity'):
                upd_values['opportunity_type'] = 'technology'
            else:
                upd_values['opportunity_type'] = 'business'
        return upd_values