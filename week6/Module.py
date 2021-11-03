"""
# 
# File          : __init__.py.py
# Created       : 27-09-2021 02:24 PM
# Author        : Varnit Rohilla
# Version       : v1.0.0
# Licensing     : (c) 2021 Varn R., LYIT
#                  Avaialable under GNU license Policy
#             
"""

import Student

modules = ['OOPR', 'DSE']

student = Student.Student('Varnit Rohilla', modules[0])


class Module(Student.Student):
    def __init__(self):
        self.module_name = student.module_taken
        self.name = student.name
