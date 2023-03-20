#coded by Kavindu Sandaruwan
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
word_list = ["advark", "baboon", "water"] #Add more words if you want
choosed_word = random.choice(word_list)
length = len(choosed_word)
print(f"Choosed word is {choosed_word}")

display_list = []
for i in range(length):
    display_list.append("_")
print(display_list)
print()

end_of_game = False
count = 6

while not end_of_game:
    guess = input("Enter a letter: ").lower()
    for position in range(length):
        letter = choosed_word[position]
        if letter == guess:
            display_list[position] = letter
    print(display_list)

    if guess not in choosed_word:
        print(stages[count])
        count -= 1

    if count == -1:
        end_of_game = True
        print()
        print(f"You lose: choosed word is {choosed_word}")

    if "_" not in display_list:
        end_of_game = True
        print()
        print("You won the game")
