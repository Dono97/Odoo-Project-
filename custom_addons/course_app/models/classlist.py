# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import Warning

class List(models.Model) :
    _name = 'list.module'
    _description = 'Class List'


    #Relationships
    l_id  = fields.Many2one('module.program', string='Module')
    student_classlist_id = fields.One2many('student.user', 'classlist_student_id', string='Student')


    #Function that displays a class list
    @api.multi
    def open_class_list(self):
        for rec in self:
            # print(rec.l_id.id)
            module = self.env['module.program'].search([('id','=',rec.l_id.id)])
            # print(module.program_module_id)
            program =  self.env['program.course'].search([('id','=',module.program_module_id.id)])

            print(program)

            print('hi')
            print(module)
            return {
                'name': ('Class List View'),
                'domain': [('program_student_id', '=', program.id)],
                'view_type': 'form',
                'res_model': 'student.user',
                'view_id': False,
                'view_mode': 'tree,form',
                'type': 'ir.actions.act_window',
                }
