# 9.1
def good():
    return print('Harry', 'Ron', 'Hermione')


good()


# 9.2
def get_odds():
    for number in range(1, 10, 2):
        yield number


count = 1
for number in get_odds():
    if count == 3:
        print("The third odd number is", number)
        break
    count += 1


# 9.3
def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func


@test
def greeting():
    print("Greeting, Earthling")


greeting()


# 9.4
class OopsException(Exception):
    pass


# raise OopsException()

try:
    raise OopsException
except OopsException:
    print('Caught an oops')


# 9.5
for thing in (f'Got {number}' for number in range(10)):
    print(thing)
