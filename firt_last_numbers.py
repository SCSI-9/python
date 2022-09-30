#Check if the first and last number of a list is the same

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

if numbers_x[0] == numbers_x[-1] and numbers_y[0] != numbers_y[-1]:
    print('Given list: ', numbers_x)
    print("result is: ",  True)
    print('Given list: ', numbers_y)
    print("result is: ",  False)
