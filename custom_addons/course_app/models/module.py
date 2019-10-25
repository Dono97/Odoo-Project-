# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import Warning

class Module(models.Model):
    _name = 'module.program'
    _description = 'Module'
    name = fields.Char('Module name', required=True)
    year = fields.Char('Module year', required=True)
    code = fields.Char('Module code', compute='compute_module_code')

    #Relationships
    program_module_id = fields.Many2one('program.course', string='Program')
    result_module_id = fields.One2many('result.module','module_result_id', string='Result')
    lecturer_module_id = fields.Many2one('lecturer.user', string='Lecturer')
    #transcript_module_id = fields.Many2one('transcript.student',string='Transcript')
    class_list_id = fields. Many2one('list.module', compute='compute_list', inverse='list_inverse', string='Class_list_id')
    class_list_ids = fields.One2many('list.module', 'l_id', string='Class_list_ids')


    #@api.multi
    #def compute_module_code(self):
    #    self.ensure_one()
    #    self.code = self.name[:3] + self.year + "0"
    #    while self.code in self:
    #        self.code = self.name[:3] + self.year + str(int(self.code[-1])+1)
    #    return self.code.upper()

    #Function to generate unique module code
    @api.depends('name')
    def compute_module_code(self):
       for rec in self:

          nametest = str(rec.name)
          namevar = nametest[:3]
          codevar = str(rec.id)
          code = namevar.upper() + codevar

          rec.code = code


    #Function that hmm....
    @api.one
    @api.depends('class_list_ids')
    def compute_transcript(self):
        if len(self.class_list_ids) > 0:
            self.class_list_id = self.class_list_ids[0]

    #Function that hmm....
    @api.one
    def list_inverse(self):
        if len(self.class_list_ids) > 0:
            # delete previous reference
            asset = self.env['list.module'].browse(self.class_list_ids[0].id)
            asset.class_list_id = False
        # set new reference
        self.class_list_id.l_id = self
