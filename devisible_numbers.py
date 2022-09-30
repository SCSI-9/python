#Display numbers divisible by 5 from a list
number=[10, 20, 33, 46, 55]
five=5

for i in number:
    if i//five:
        print(i)
    else:
        print("Number does not devisible by 5")

