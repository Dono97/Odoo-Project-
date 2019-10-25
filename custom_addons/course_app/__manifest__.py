# -*- coding: utf-8 -*-
{

    'name': 'Course management',
    'description': 'Creating modules, programs and loading students ',
    'author': 'FTB Tech',
    'depends': ['base', 'website'],
    'application': True,
    'data': [
        'security/course_security.xml',
        'security/results_security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/course_menu.xml',
        'views/results_menu.xml',
        'views/module_view.xml',
        'views/program_view.xml',
        'views/student_view.xml',
        'views/transcript_view.xml',
        'views/upload_results_view.xml',
        'views/load_lecturer_view.xml',
        'views/classlist_view.xml'
    ],

}
