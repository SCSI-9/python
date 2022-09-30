# This simple programm will calculate your ability to rolling for courses

from unittest import result
from xml.etree.ElementPath import get_parent_map
import  os
import  csv


gpa = float(input('What is your last gpa score? '))
lowest_grade = float(input('What is your lowest grade? '))

def gpa_pass ():
    if gpa >= 80 and lowest_grade >= 70:
        return('Sucess! You have enrolled!')
    else:
        return('Sorry! But your score is too low!')

output_1 = (gpa_pass());

def one_more_chance():
    if output_1 == 'Sorry! But your score is too low!':
        return("Dont worry I will give you one more chance")
    else:
        print('Good Job!')

result = (one_more_chance());

print(result)