# 6.1 Use a for loop to print the values of the list [3,2,1,0]
for x in list(range(3,-1,-1)):
    print(x)

# 6.2 
guess_me = 7
number = 1

while True:
    if number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break
    else:
        print(f'{number} is too low')
        number += 1

# 6.3
guess_me = 5

for number in range(10):
    if number < guess_me:
        print(f'{number} is too low')
    elif number == guess_me:
        print('found it!')
        break
else:
    print('oops')
