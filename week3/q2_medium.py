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
print(week1)
print(week2)
TOTAL_PEOPLE = week1 + week1


def random_lotto_numbers():
    random_lotto_numbers = []
    for i in range(1, 21):
        random_lotto_numbers.append(random.randrange(1, 20))
    # print(random_lotto_numbers)
    return random_lotto_numbers


random_lotto_numbers = random_lotto_numbers()


def assign_lotto_number():
    week1_lotto_numbers = {}
    for j in week1:
        week1_lotto_numbers[j] = random.choice(random_lotto_numbers)

    week2_lotto_numbers = {}
    for k in week2:
        week2_lotto_numbers[k] = random.choice(random_lotto_numbers)

    print(week1_lotto_numbers)
    print(week2_lotto_numbers)
    return [week2_lotto_numbers, week2_lotto_numbers]


lotto_numbers = assign_lotto_number()


# query 1 : Find the intersection in the lists to find out who bought tickets on both weeks

def common_people():
    common_people = []
    for i in week1:
        for j in week2:
            if i == j:
                common_people.append(i)
    print(common_people)
    return common_people


common_people = common_people()


# query 3 : Create a list of the unique members who have played over the two weeks
def unique_people():
    unique_people = []
    for i in TOTAL_PEOPLE:
        # print(i)
        if i in common_people:
            # print('inif')
            continue
        else:
            # print('inelse')
            unique_people.append(i)
    print(unique_people)


# query 3 : What were the most common lotto numbers
def most_common_lotto_numbers():
    frequency = 1
    common_numbers = {}
    for i in lotto_numbers[0]:
        i = str(lotto_numbers[0][i])
        if i in common_numbers:
            common_numbers[i] = common_numbers[i] + 1
            frequency = 1
        else:
            common_numbers[i] = frequency
            frequency = 1

    for j in lotto_numbers[1]:
        j = str(lotto_numbers[1][j])
        if j in common_numbers:
            common_numbers[j] = common_numbers[j] + 1
            frequency = 1
        else:
            common_numbers[j] = frequency
            frequency = 1

    print(common_numbers)
    print('most common lotto numbers:', end="\t")
    for i in common_numbers:
        if common_numbers[i] > 1:
            print(i, end="\t")


most_common_lotto_numbers()


# query 4 :Did any member pick the same number on multiple occasions
def same_number_multiple_occasions():
    for i in common_people:
        if i in lotto_numbers[0]:
            if i in lotto_numbers[1]:
                if lotto_numbers[0][i] == lotto_numbers[1][i]:
                    print('Yes')
                    break
                else:
                    print('No')


same_number_multiple_occasions()
