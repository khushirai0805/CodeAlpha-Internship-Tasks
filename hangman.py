import random

words = ["apple", "mango", "banana", "orange", "grapes"]
word = random.choice(words)
print("Word selected!")

blanks = ["_"]*len(word)
print(" ".join(blanks))

attempts = 6  # number of wrong guesses allowed

while attempts > 0 and "_" in blanks:
    print("\nAttempts left:", attempts)
    print(" ".join(blanks))
    
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                blanks[index] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong guess!")

print("\nFinal word:", word)
if "_" not in blanks:
    print("🎉 You win!")
else:
    print("❌ You lose!")

