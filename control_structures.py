# Control Structures / Control Flow


# If Statements

# if condition:
    # code to execute if another_condition is True
# elif another_condition:
    # code to execute if another_condition is True
# else:
    # code to execute if all condintions are False

# instance_running = "running"

#if instance_running == "running":
    #print("The ec2 is running")
#elif instance_running == "stopped":
    #print("The ec2 is stopped...")
#else:
    #print("The ec2 instance is in an unexpected state")

public_access_block = True
if public_access_block == True :
    print("This s3 bucket is secure")
else:
    print("This s3 bucket is not secure")
