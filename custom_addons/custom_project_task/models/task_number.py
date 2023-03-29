from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)

class ProjectTask(models.Model):
    #inherited from 'project.task' model
    _inherit = 'project.task'

    code = fields.Char(string = "Reference", related='analytic_account_id.code', readonly=False)
    task_number = fields.Char(string = "Task Number", readonly=True)
    task_id = fields.Char(string = "Task Number", compute='_computed_task_id', readonly=True)

    # priority selection field (added, used for Kanban view)
    priority = fields.Selection([('0', 'Normal'), 
                                 ('1', 'Medium priority'), 
                                 ('2', 'High priority'), 
                                 ('3', 'Urgent')], 
                                 string='Priority')


    #sequence number    
    @api.model  
    def create(self, vals):
        vals['task_number'] =self.env['ir.sequence'].next_by_code('project.task')
        return super(ProjectTask, self).create(vals)
    

    #using computed filed to get code & task_number
    @api.depends('code', 'task_number')
    def _computed_task_id(self): 
            for task in self:
                task.task_id = str(task.code) + str(task.task_number)


    def name_get(self):
        result = []
        for task in self:
            result.append((task.id, "%s (%s)" % (task.name, task.task_id)))
            # _logger.info("**task.name********************** %s", task.name)
        return result



 