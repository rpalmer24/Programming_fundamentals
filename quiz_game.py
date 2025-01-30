print("Welcome to the AWS Quiz")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    #Converts the user input to lower case. If the is not "yes" the program will quit
    quit()

print("Let's play!")

score = 0

answer = input ("What Does AWS IAM stand for?")
if answer.lower() == "identity and access management":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What AWS secrive can you use to balance internet traffic across EC2s?")
if answer.lower() == "elastic load balancer":
    print ("You got it!")
    score += 1
else:
    print("That's incorrect")

answer = input("What does AWS stand for?")
if answer.lower() == "amazon web services":
    score += 1
else:
    print("Incorrect")

answer = input("What AWS service is used to run code without provisioning or managing servers?")
if answer.lower() == "lambda":
    print("Correct!")
    score += 1
else:
    print("Sorry, that is incorrect!")

print("Finished!")
print("You got " +   str(score)  + " out of 4 question correct!")
