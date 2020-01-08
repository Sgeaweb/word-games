import random

import define

word_bank = []
with open("word_list.txt", "r") as bank:
	for i in bank:
		if "\n" in i:
			a = i.split("\n")
			word_bank.append(a[0].lower())
		else:
			word_bank.append(i)

rand_word = random.randint(1, len(word_bank) - 1)
word = word_bank[rand_word]
visible = []

for make_invisible in word:

	visible.append("_")


game = True
strikes = 0
win = None

while game:
	print(*visible)
	

	guess = input("Guess a letter: ")

	if guess in word:
		for num, letter in enumerate(word):
			if letter == guess:
				visible[num] = word[num]
		if "_" not in visible:
			game = False
			print("You win.")
			print(word)
			win = True
	else:
		strikes += 1
		print("Strikes: " + str(strikes))
		if strikes == len(word):
			game = False
			print("You lose.")
			print(word)
			win = False

	

define.definition(word)