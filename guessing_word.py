import random

animals = {'elephant', 'tiger', 'lion', 'zebra', 'giraffe', 'monkey', 'crocodile', 'kangaroo'}
fruits = {'apple', 'banana', 'orange', 'grapes', 'watermelon', 'pineapple', 'mango', 'strawberry'}
stationary = {'pencil', 'pen', 'eraser', 'sharpener', 'ruler', 'scale', 'compass', 'calculator'}

# Combine all sets into a list
words = list(animals) + list(fruits) + list(stationary)

random_word = random.choice(words)
print("Word Guessing Game")
if random_word in animals:
    print("Hint: The word is an animal")
elif random_word in fruits:
    print("Hint: The word is a fruit")
else:
    print("Hint: The word is stationary")

user_guesses = ''
chances = 5

while chances > 0:
    wrong_guesses = 0
    for ch in random_word:
        if ch in user_guesses:
            print(ch, end=' ')
        else:
            print('_', end=' ')
            wrong_guesses += 1

    if wrong_guesses == 0:
        print('\nCongratulations, you won! The word is', random_word)
        break

    guess = input("\nMake a guess: ")
    user_guesses += guess.lower()  # Convert guess to lowercase to handle case insensitivity
    if guess.lower() not in random_word:
        chances -= 1
        print(f"Wrong. You have {chances} more chances left.")
        if chances == 0:
            print("Game over. You lose. The word was", random_word)
