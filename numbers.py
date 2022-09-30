# This programme will execute the numbers and show you the previous number

print ('Printing current and previous number sum in a range(10)')

previous_num = 0

for i in range(1,25):
    x_sum = previous_num + i 
    print('Current Number' ,i, 'Previous Number', previous_num,  'Sum:', x_sum )

    previous_num = i