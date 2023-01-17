
import random

guessesTaken = 0

print('Hello, whats your name?')
myname = input()

number = random.randint(1, 20)
print('Well, ' + myname + ' I am thinking of a number between 1 and 20.')

for guessesTaken in range(6):
    print('take a guess')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low')

    if guess > number:
        print('Your number is too high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job ' + myname + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')


