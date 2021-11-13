# Initial variable to track game play
user_play = "y"
old_num = 0
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_choice = int(input("How many numbers?"))

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(user_choice):
        # Print each number in the range
        print(old_num + x)

    # Once complete...
    old_num = old_num + user_choice
    #print(old_num)
    user_play = input("Continue: (y)es or (n)o? ")