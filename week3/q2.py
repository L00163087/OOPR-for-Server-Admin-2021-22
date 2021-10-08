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
import random

if __name__ == '__main__':
    '''

   Main method of application 



   Linear programming only presented here wrt demo of lists



   Parameters:

    none



   Returns:

    none

  '''

    week1 = ['Joe', 'John', 'Jane', 'Mick', 'Mary', 'Ann', 'Rick', 'John', 'Aine', 'Brenda']
    week2 = ['Jack', 'Mary', 'Phil', 'John', 'Pat', 'Joe', 'Luke', 'Bill', 'Ben', 'Nathan']
    TOTAL_PEOPLE = week1 + week1
    RANDOM_NUMBERS = []

    for i in range(1, 21):
        RANDOM_NUMBERS.append(random.randrange(1, 20))
    # print(RANDOM_NUMBERS)

    week1_dict = {}
    for i in week1:
        week1_dict[i] = random.choice(RANDOM_NUMBERS)

    week2_dict = {}
    for i in week2:
        week2_dict[i] = random.choice(RANDOM_NUMBERS)

    print(week1_dict)
    print(week2_dict)

    # query 1 : Find the intersection in the lists to find out who bought tickets on both weeks
    both_weeks = []
    for i in week1:
        for j in week2:
            if i == j:
                both_weeks.append(i)

        # query 3 : What were the most common lotto numbers
        number = 0
        common_number = {}
        for i in week1_dict:
            if week1_dict[i] in common_number:
                week1_dict[i] = week1_dict[i] + 1
            else:
                week1_dict[i] = number

        #
#     lotto_numbers = {}
# for i in TOTAL_PEOPLE:
#     lotto_numbers[i] = random.randrange(1, 20)
#
# print('people who bought  tickets on both weeks:')
# for name in lotto_numbers:
#     print(name)
