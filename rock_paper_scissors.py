import random

user = 0
computer = 0

choices = ["rock","paper","scissors"]
#choices[0] use index to give the choices numeric value

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break #break out of loop
    
    # if user_input not in ["rock","paper","scissors"]: <-- this was the orginal code before adding the choice variable
    if user_input not in choices:    
        continue 
        #if user input is not in the list than it will ask again/run previous coode

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_choice = choices[random_number]
    print("Computer's choice", computer_choice)

    if user_input == "rock" and computer_choice == "scissors":
        print("You won!")
        user += 1
    elif user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        user += 1
    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user += 1
    elif user_input == computer_choice:
        print ("It's a tie!")
    
    else:
        print("You lost!")
        computer += 1 

print("You won ", user, " times")
print("Computer won ", computer, " times")

print("Bye!")

        
