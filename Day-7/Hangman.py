import random
import logo,word_list,Stages

print(logo.logo)


chosen_word = random.choice(word_list.word_list)
# print(f"Chosen word: {chosen_word}")

display = []
for letter in chosen_word:
    display.append("-")
print(display)

lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost!")

    print(display)

    if "-" not in display:
        end_of_game = True
        print("You win!")

    print(Stages.stages[lives])
