# -*- coding: utf-8 -*-
from odoo import http, api, fields, models

class StudentTranscriptRequest(http.Controller):

    @http.route('/transcript_request', auth='public')
    def transcript_request(self, **kw):
        user = http.request.env['res.users'].search([('id', 'like', http.request.session.uid)])
        # return str(user.id) # 13
        # return user.login # Working - SU num
        student = http.request.env['student.user'].search([("student_number", 'like', user.login)])
        # return str(student.student_number) # Working - Logged in SU num

        mark = http.request.env['result.module'].search([('student_result_id.student_number', 'like', student.student_number)]) # Workings
        #print(mark.module_result_id)
        #module = http.request.env['module.program'].search(['name', 'like', mark.module_result_id.name])
        return http.request.render('course_app.transcript_request', {
            'student': student, 'mark': mark, #'module': module
        })



#'value[student_result_id.student_number]', '=', value[http.request.uid]


# class ./admin(http.Controller):
#     @http.route('/./admin/./admin/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./admin/./admin/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./admin.listing', {
#             'root': '/./admin/./admin',
#             'objects': http.request.env['./admin../admin'].search([]),
#         })

#     @http.route('/./admin/./admin/objects/<model("./admin../admin"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./admin.object', {
#             'object': obj
#         })
