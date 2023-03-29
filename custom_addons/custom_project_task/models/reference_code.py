from odoo import api, models, fields

class ProjectProject(models.Model):
    _inherit = 'project.project'

    code = fields.Char(string = "Reference", related='analytic_account_id.code', readonly=True)

