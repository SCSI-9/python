# def sequence(n):
#     while n != 1:
#         print(n)
#         if n % 2 == 0: # n = четное значение
#             n = n / 2
#         else: # n = нечетное значение
#              n = n*3 + 1

# sequence(16)

# count=0
# word='banana'

# for letter in word:
#     if letter == 'a':
#         count=count + 1
# print(count)

word1='orange'
word2='grapefruit'

def for_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

for_both(word1,word2)



