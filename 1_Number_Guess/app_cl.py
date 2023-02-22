import random

class NumberGuesser:
    def __init__(self, max_num=100):
        self.number = random.randint(1, max_num)
        self.max_num = max_num
        self.num_guesses = 0
        
    def guess(self, number):
        self.num_guesses += 1
        if number > self.number:
            return "Too high!"
        elif number < self.number:
            return "Too low!"
        else:
            return "You got it!"

if __name__ == "__main__":
    max_num = int(input("Enter the maximum number for the game: "))
    game = NumberGuesser(max_num)
    
    while True:
        guess = int(input(f"Guess a number between 1 and {max_num}: "))
        result = game.guess(guess)
        print(result)
        
        if result == "You got it!":
            print(f"It took you {game.num_guesses} guesses.")
            
            play_again = input("Do you want to play again? (y/n) ")
            if play_again.lower() == "y":
                max_num = int(input("Enter the maximum number for the game: "))
                game = NumberGuesser(max_num)
            else:
                print("Good bye!, will see you next time!")
                break