from random import randint


num = randint(1, 100)
guessed = False

while not guessed:
    ans = input('Enter a number: ')


    if int(ans) == num:
        print('Correct!')
        break

    elif int(ans) > num:
        print('number too big')
    
    elif int(ans) < num:
        print('number too small')