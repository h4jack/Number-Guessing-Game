import random

class NumberGuessingGame:
    def __init__(self):
        self.max_range = 0
        self.game_mode = 0

    def start(self):
        print("Welcome to the Number Guessing Game!")
        self.choose_mode()
    
    def choose_mode(self):
        print("Select mode:")
        print("1. Robot Guesses (You think of a number)")
        print("2. You Guess (Robot thinks of a number)")
        print("3. Robot Auto Guesses (You think of a number)")
        print("0. Exit")
        self.game_mode = self.get_input("Enter the number corresponding to the mode you want to play: ", 0, 3)
        
        if self.game_mode == 0:
            print("Exiting the game. Goodbye!")
            return
        
        self.set_max_range()
        
        if self.game_mode == 1:
            self.robot_guesses()
        elif self.game_mode == 2:
            self.user_guesses()
        elif self.game_mode == 3:
            self.robot_auto_guesses()

    def set_max_range(self):
        if self.game_mode == 1 or self.game_mode == 2:
            print("Select difficulty level:")
            print("1. Easy (1-100)")
            print("2. Normal (1-1000)")
            print("3. Medium (1-10000)")
            print("4. Hard (1-100000)")
            self.max_range = 10 ** self.get_input("Enter the number corresponding to the difficulty level: ", 1, 4)
        elif self.game_mode == 3:
            self.max_range = 10 ** random.randint(2, 5)
    
    def get_input(self, prompt, min_val=None, max_val=None):
        while True:
            try:
                user_input = int(input(prompt))
                if (min_val is None or user_input >= min_val) and (max_val is None or user_input <= max_val):
                    return user_input
                else:
                    print("Please enter a valid number within the specified range.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def robot_guesses(self):
        print(f"Think of a number between 1 and {self.max_range}")
        input("Press Enter when ready...")
        
        num_guesses = 0
        low, high = 1, self.max_range
        while True:
            guess = random.randint(low, high)
            print(f"I guess the number is: {guess}")
            num_guesses += 1
            response = input("Is it (h)igher, (l)ower, or (c)orrect? ").lower()
            if response == 'c':
                print(f"Guessed correctly! The number is {guess}. It took me {num_guesses} guesses.")
                break
            elif response == 'h':
                high = guess - 1
            elif response == 'l':
                low = guess + 1

    def user_guesses(self):
        target_number = random.randint(1, self.max_range)
        print(f"I've chosen a number between 1 and {self.max_range}. Try to guess it!")
        
        num_guesses = 0
        while True:
            guess = self.get_input("Your guess: ", 1, self.max_range)
            num_guesses += 1
            
            if guess == target_number:
                print(f"Congratulations! You guessed the correct number {target_number} in {num_guesses} guesses!")
                break
            elif guess < target_number:
                print("Too low. Try again!")
            else:
                print("Too high. Try again!")

    def robot_auto_guesses(self):
        target_number = random.randint(1, self.max_range)
        print(f"Think of a number between 1 and {self.max_range}")
        input("Press Enter when ready...")
        
        num_guesses = 0
        low, high = 1, self.max_range
        while True:
            guess = random.randint(low, high)
            print(f"I guess the number is: {guess}")
            num_guesses += 1
            if guess == target_number:
                print(f"Guessed correctly! The number is {guess}. It took me {num_guesses} guesses.")
                break
            elif guess < target_number:
                print("My guess is too low.")
                low = guess + 1
            else:
                print("My guess is too high.")
                high = guess - 1

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start()
