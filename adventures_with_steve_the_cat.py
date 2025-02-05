print ("""Welcome to the Adventures with Steve the Cat!
       My name is Steve the Cat! Steve for short. I can really use some help.""")

name = input("What is your name?: ")
print(f"Hey {name}, let's get started") 

print("I'm looking for my favorite blue mouse toy, but can't remember where I put it.")

# Originally did this as if/elif/else then decided to switch to while loops
# Flags help track conditions and make decisions based on specific tates

living_room_first = None  
found_toy = False  # Track if the toy has been found

# Room Selection
while True:
    answer = input("Where should I check first, the living room or dining room? ").lower()

    if answer == "living room":
        print("Okay, let's go to the living room")
        living_room_first = True
        break # to break loop and move to the next

    elif answer == "dining room":
        print("Let's check the dining room")
        living_room_first = False
        break

    else:
        print("That's not a choice. Please choose living room or dining room.")

# Living Room Loop 
if living_room_first:  
    answer = input("I think I see something under the coffee table. Should we check it out? Type yes or no: ").lower()

    if answer == "yes":
        print("Nope, just a sock. Let’s keep searching!")

    # Ask about the sofa next
    answer = input("Should we check the sofa? Type yes or no: ").lower()

    if answer == "yes":
        print("Found it! Now I can play.")
        found_toy = True  # toy as found

    elif answer == "no":
        print("Alright, let's keep looking!")

# Transition to the dining room happens
if not found_toy:
    print("Alright, let's check the dining room!") 

    while True: 
        answer = input("Oh, the humans are eating! Should we quickly check under the table? Type yes or no: ").lower()
        
        if answer == "yes":
            print(f"Found it! I had a feeling I left it there. Thank you, {name}!")
            found_toy = True
            break
        elif answer == "no":
            print("Okay, maybe next time.")
            break
        else:
            print("Please answer yes or no.")

print("That was a lot of moving around. I'm ready for another nap. Thanks for your help. Bye!")

"""
Notes:

Flags:
living_room_first = None  --> stores whether or not user is choose living or dining room
found_toy = False --> let us know if the toy has been found (true = yes, falso = no)

While Loop:
ensure users put in valid response
living_room_first = True --> runs through the living room loop
living_room_first = False --> jumps to dining room loop
"""