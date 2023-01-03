import random

words = ["aarav","mohit","bhanu","dia", "deeksha", "shreya"]
random_word = random.choice(words)
print(random_word)
word_length = len(random_word)

display = []
lives = 6
end_of_game = True

for _ in range(word_length):
    display.append("_")
print(display)

while end_of_game:
    guess = input("Enter a letter: ").lower()
    for position in range(word_length):
        letter = random_word[position]
        if (guess == letter):
            display[position] = guess

    if guess not in random_word:
        lives -= 1
        if (lives == 0):
            end_of_game = False
            print("You lose")

    if '_' not in display:
        end_of_game = False
        print("You win!")

    # print(f"lives value is {lives}")
    print(f"{display}")
    print(f"{''.join(display)}")





    
