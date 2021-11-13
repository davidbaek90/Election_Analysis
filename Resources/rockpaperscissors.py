# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection

print(computer_choice)
# Run Conditionals
if computer_choice == "r" and user_choice == "r":
    print('It is a tie!')
elif computer_choice == "r" and user_choice == "p":
    print('You won!')
elif computer_choice == "r" and user_choice == "s":
    print('You lost!')
elif computer_choice == 'p' and user_choice == 'p':
    print('It is a tie!')
elif computer_choice == "p" and user_choice == "r":
    print('You won!')
elif computer_choice == "p" and user_choice == "s":
    print('You lost!')
elif computer_choice == 's' and user_choice == 's':
    print('It is a tie!')
elif computer_choice == "s" and user_choice == "p":
    print('You won!')
elif computer_choice == "s" and user_choice == "r":
    print('You lost!')