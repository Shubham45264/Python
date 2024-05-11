import random
f=open("words.txt", "r")
data=f.readline()
words=data.split()
word=random.choice(words)
#words = ["UMBRELLA","COMPUTER","TELESCOPE","SMARTPHONE"]
word = random.choice(words)
total_chances = 7
guessed_word = "-"*len(word)
while total_chances != 0:
  print(guessed_word)
  letter = input("Enter a letter: ").upper()
  if letter in word:
   for index in range(len(word)):
      if word[index] == letter:
        guessed_word = guessed_word[:index] + letter + guessed_word[index+1:]
     # print(guessed_word)
  if guessed_word == word:
    print("Congratulations, you won!")
    break
else:
  print("Game Over")
  print("You Lose")
  print("All the chances are over")
print("The correct word is",word)