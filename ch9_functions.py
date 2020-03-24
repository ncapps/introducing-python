# 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

# 9.2
def get_odds():
    for number in range(1, 10, 2):
            yield number

count = 1
for odd in get_odds():
    if count == 3:
        print(f"Third odd number is {odd}")
        break
    else:
        count += 1


# 9.3
def test(func):
    def inner_function(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return inner_function

@test
def test2():
    print('middle')

test2()

#9.4
class OopsException(Exception):
    pass

numbers = [1, 2, 3, 4, 5]

for n in numbers:
    try:
        if n == 4:
            raise OopsException
        else:
            print(n)
    except OopsException as exc:
        print('Caught an oops')