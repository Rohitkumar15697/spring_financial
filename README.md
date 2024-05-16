# spring_financial
Odoo CRM Customization and Odoo Web API's


# CRM Lead Customization:
- Opportunity Type and other field are added in opportunity form view [screenshot](https://prnt.sc/6D3FgXGjJFBD) , [screenshot](https://prnt.sc/ddFEyQurPcff)
- Lead can not convert to opportunity if not in Complete State [screenshot](https://prnt.sc/zJv-haJlYAlw)
- Button to mark lead as complete [screenshot](https://prnt.sc/HTbKicDb0VTG)
- When we will click on create opportunity [screenshot](https://prnt.sc/xL8YRg-_jgc2) one extra opportunity will be created with opportunity type as 'Technical' default opportunity will be as 'Business' Type.
- Note: It will work for Conversion Action as 'Convert to opportunity' option [screenshot](https://prnt.sc/QZN7qHMuXsG1)
- It will show a wizard to mark as complete when we convert one lead to opportunity and if it is not in complete stage [screenshot](https://prnt.sc/_rxFg-xjwfik).

# Postman API's
- Added a controller to handle http request and create contact from postman with contact data in json.
- Searching countries using jsonrpc.

# many2many_tags widget:
- Selection field is visible at the start of records https://prnt.sc/BVZXqUW0Q23O
- We can select multiple records in Many2many field at one time.
