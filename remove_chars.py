#Remove first n characters from a string

from operator import le
import string

word=input('Tell me something: ')
length=len(word) - 1

number=int(input('Write some number: '))

if number < length:
        print(word[number:])
else:
    print('Bad Number!')

    


   