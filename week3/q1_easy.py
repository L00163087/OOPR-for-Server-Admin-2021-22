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
if __name__ == '__main__':
    '''

   Main method of application 


   Linear programming only presented here wrt demo of lists


   Parameters:

    none


   Returns:

    none

  '''
    
student1 = 'L00001'
student2 = 'L00002'

module1 = 'Java_oo_programming'
module2 = 'Python_Scripting'

STUDENT_NUMBER = 'student_number'
GRADE = 'grade'

students_enrolled = (student1, student2)
modules = [module1, module2]
grades_module1 = [{STUDENT_NUMBER: student1, GRADE: 59.3}, {STUDENT_NUMBER: student2, GRADE: 63.5}]
grades_module2 = [{STUDENT_NUMBER: student2, GRADE: 66.78}, {STUDENT_NUMBER: student2, GRADE: 69.5}]

INPUT_MODULE = input('Enter the module name(Java_oo_programming or Python_Scripting): ')

if INPUT_MODULE == modules[0]:
    for i in grades_module1:
        print('Student id:' + i[STUDENT_NUMBER] + '\nGrade: ' + str(i[GRADE]))
elif INPUT_MODULE == modules[1]:
    for i in grades_module2:
        print('Student id:' + i[STUDENT_NUMBER] + '\nGrade: ' + str(i[GRADE]))
