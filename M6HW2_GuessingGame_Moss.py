# In this assignment, you will create a simple computer game in Python.
# November 12, 2017
# CTI-110 M6HW2_Random Number Game
# Donald Moss

import random

def start_guess():
    random_number = random.randrange(0, 101)
    print("Random number has been generated.")

    while True:
        try:
            user_input = int(input("Your guess please: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if user_input == random_number:
            print("Well done!")
            break
        elif not 0 <= user_input <= 100:    # If it's not between 0 to 100
            print("Our guess range is between 0 and 100, please try a bit {}."
                # User_input at this point must be outside the range
                # so if it's not below the min, it's definitely above the max
                 .format("higher" if user_input < 0 else "lower"))
        else:
            print("Try one more time, a bit {}."
                # User_input at this point must be inside the range
                # so if it's not below the random_number, it's definitely above it
                 .format("higher" if user_input < random_number else "lower"))


if __name__ == '__main__':
    start_guess()
    print("End of program.")     
