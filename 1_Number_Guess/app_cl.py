import random

class NumberGuesser:
    def __init__(self, max_num=100):
        #picking a randomnumber between 1 and max_num
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
    #getting the maximum number from the user
    max_num = int(input("Enter the maximum number for the game: ")) 
    game = NumberGuesser(max_num) #creating an instance of the NumberGuesser class
    
    while True:
        #getting the user's guess
        guess = int(input(f"Guess a number between 1 and {max_num}: ")) 
        #calling the guess method
        result = game.guess(guess) 
        print(result) 
        
        if result == "You got it!": 
            #checking if the user got the number right
            print(f"It took you {game.num_guesses} guesses.") 
            
            play_again = input("Do you want to play again? (y/n) ") 
            #checking if the user wants to play again
            if play_again.lower() == "y": 
                max_num = int(input("Enter the maximum number for the game: ")) 
                game = NumberGuesser(max_num)
            else:
                print("Good bye!, will see you next time!") 
                break