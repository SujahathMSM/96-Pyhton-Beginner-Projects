import random

class NumberGuesser:
    def __init__(self, max_num=100):
        self.number = random.randint(1, max_num) #picking a randomnumber between 1 and max_num
        self.max_num = max_num
        self.num_guesses = 0 # initialising the number of guesses to 0
        
    def guess(self, number):
        self.num_guesses += 1
        if number > self.number:
            return "Too high!"
        elif number < self.number:
            return "Too low!"
        else:
            return "You got it!"

if __name__ == "__main__":
    max_num = int(input("Enter the maximum number for the game: ")) #getting the maximum number from the user
    game = NumberGuesser(max_num) #creating an instance of the NumberGuesser class
    
    while True:
        guess = int(input(f"Guess a number between 1 and {max_num}: ")) #getting the user's guess
        result = game.guess(guess) #calling the guess method
        print(result) #printing the result
        
        if result == "You got it!": #checking if the user got the number right
            print(f"It took you {game.num_guesses} guesses.") #printing the number of guesses
            
            play_again = input("Do you want to play again? (y/n) ") #asking the user if they want to play again
            if play_again.lower() == "y": #checking if the user wants to play again
                max_num = int(input("Enter the maximum number for the game: ")) #getting the maximum number from the user
                game = NumberGuesser(max_num)
            else:
                print("Good bye!, will see you next time!") #printing a goodbye message
                break