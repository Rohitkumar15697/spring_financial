import json
from logging import getLogger

from odoo.http import route, request, Controller

class HttpController(Controller):
    @route('/contact/create', type='http', methods=['POST'], auth="public", csrf=False)
    def create_contact(self, *args, **kwargs):
        status = "Error"
        message = ''
        try:
            data = eval(request.httprequest.data.decode('utf-8'))
            if data:
                    contact_data = self.prepare_contact_data(data)
                    contact = request.env['res.partner'].sudo().create(contact_data)
                    if contact:
                        message = 'Contact Created Successfully!'
                        status = "Success"
        except Exception as e:
            message = str(e)
        return json.dumps({'code': status, 'message': message})
    
    def prepare_contact_data(self, data):
        country = data.get('country')
        state = data.get('state')
        country_id, state_id = self.get_country_state(country, state)
        return {
                'name': data.get('name'),
                'email': data.get('email'),
                'phone': data.get('phone'),
                'street': data.get('street'),
                'city': data.get('city'),
                'zip': data.get('zip'),
                'state_id': state_id,
                'country_id': country_id
                }

    def get_country_state(self, country, state):
        country_id, state_id = False, False
        if country:
            country_id = request.env['res.country'].search(['|', ('name','ilike',country),('code', 'ilike', country)], limit=1).id
        if state:
            state_id = request.env['res.country.state'].search(['|',('name','ilike', state),('code','ilike', state)], limit=1).id
        return country_id, state_id
