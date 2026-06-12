import random

def main():
    words = ["python", "stanford", "code", "robot"]
    word = random.choice(words)
    guesses = ""
    turns = 5
    print("Welcome to Word Guessing Game!")

    while turns > 0:
        failed = 0
        display = ""
        for char in word:
            if char in guesses:
                display += char
            else:
                display += "_"
                failed += 1
        print("Word: " + display)
        
        if failed == 0:
            print("You Win!")
            break
            
        guess = input("Guess a letter: ").lower()
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong! Turns left: " + str(turns))

if __name__ == '__main__':
    main()
