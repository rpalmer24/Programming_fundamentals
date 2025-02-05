print ("""Welcome to the Adventures with Steve the Cat!
       My name is Steve the Cat! Steve for short. I can really use some help.""")

name = input("What is your name?: ")
print(f"Hey {name}, let's get started") 

print("I'm looking for my favorite blue mouse toy, but can't remember where I put it.")

# Flags to track room choice and toy discovery
living_room_first = None  
found_toy = False  # Track if the toy has been found

# Room selection
while True:
    answer = input("Where should I check first, the living room or dining room? ").lower()

    if answer == "living room":
        print("Okay, let's go to the living room")
        living_room_first = True
        break 

    elif answer == "dining room":
        print("Let's check the dining room")
        living_room_first = False
        break

    else:
        print("That's not a choice. Please choose living room or dining room.")

# **Living Room Exploration** (only if chosen first)
if living_room_first:  
    answer = input("I think I see something under the coffee table. Should we check it out? Type yes or no: ").lower()

    if answer == "yes":
        print("Nope, just a sock. Let’s keep searching!")

    # Ask about the sofa next
    answer = input("Should we check the sofa? Type yes or no: ").lower()

    if answer == "yes":
        print("Found it! Now I can play.")
        found_toy = True  # Mark toy as found

    elif answer == "no":
        print("Alright, let's keep looking!")

# **Ensure transition to the dining room happens correctly**
if not found_toy:
    print("Alright, let's check the dining room!")  # Transition message

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
