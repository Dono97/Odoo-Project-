from odoo import fields, models, api

class Result(models.Model):
    _name = 'result.module'
    _description = 'Result'
    value = fields.Float('Result Value', required=True)
    user_id = fields.Many2one('res.user', string='User', readonly=True, states={'draft': [('readonly', False)]}, default=lambda self: self.env.user)
    pass_grade = fields.Char('Pass grade', compute = "generate_pass_grade")



    #Relationships
    module_result_id = fields.Many2one('module.program', string='Module', required=True)
    student_result_id = fields.Many2one('student.user', string='Student', required=True)
    #transcript_result_id = fields.Many2one('transcript.student', string='Transcript')


    @api.depends('value')
    def generate_pass_grade(self):
        for rec in self:
            if rec.value >= 50:
                rec.pass_grade = "Pass"
                pass_grade = rec.pass_grade

            else:
                rec.pass_grade = "Fail"
                pass_grade = rec.pass_grade
