import random
# Guess the number game

generated = random.randint(0, 100)
guess = 0

print("Let's play a game, it's called 'Guess the number'.")
print('I will choose a number between 1 and 100.\nIf you want to exit the game at any time type: quit')

while True:
    guess = input('Pick a number: ')
    if guess == 'quit':
        print('Exit Game')
        break
    try:
        val = int(guess)
        if (val < 0) or (val > 100):
            print('The number must be between 0 and 100')
        elif val < generated:
            print("Caut un numar mai mare")
        elif val > generated:
            print("Caut un numar mai mic")
        else:
            print('Corect!')
            break
    except ValueError:
        print("Pick a number between 0 and 100 or type quit to Exit")


