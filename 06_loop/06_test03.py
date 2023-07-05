guess_me = 5
for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('fount it!')
        break
    else:
        print('Oops!')
        break
