from odoo import models, fields, api
from odoo.exceptions import UserError


class Lead(models.Model):
    _inherit = "crm.lead"

    lead_stage_id = fields.Many2one('crm.lead.stage', 
                                    readonly=False,
                                    ondelete='restrict', 
                                    store=True
                                )

    opportunity_type = fields.Selection([
        ('technology', 'Technology'),
        ('business', 'Business'),
    ], string="Opportunity Type")
    
    technology_name = fields.Char(string="Technology Name")
    business_name = fields.Char(string="Business Name")
    
    is_lead_complete = fields.Boolean()
    
    @api.model
    def is_complete_available(self):
        """It will return Complete stage if available to select or not
        """
        return self.env['crm.lead.stage'].search([('name','=', 'Complete')], limit=1)

    @api.constrains('lead_stage_id')
    def change_stage_id(self):
        completed = False
        if self.lead_stage_id.name == 'Complete':
            completed = True
        self.is_lead_complete = completed

    def mark_lead_as_complete(self):
        """Mark lead as complete if Complete is available to select
        """
        complete_available = self.is_complete_available()
        if complete_available:
            self.lead_stage_id = complete_available.id
            self.is_lead_complete = True
        else:
            raise UserError('Complete stage in not available in the lead stages!')

    def return_completion_wizard(self):
        """Return a Lead Completion Wizard to mark lead as complete
        """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Complete Leads Stage',
            'res_model': 'lead.complete.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_lead_id': self.id},
        }

    def convert_opportunity(self, partner, user_ids=False, team_id=False):
        """Override complete method based on context to get the required customization flow
        """
        if not self._context.get('opportunity_customization') or not self.is_complete_available():
            return super().convert_opportunity(partner, user_ids, team_id)

        # Create one extra opportunity of opportunity type 'technology'
        customer = partner if partner else self.env['res.partner']
        for lead in self:
            if lead.is_lead_complete:
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
