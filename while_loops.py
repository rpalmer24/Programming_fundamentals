#count = 0
#while count < 5:
#    print(f"count is: {count}")
#    count += 1

import random
import time

def stimulate_instance_state():
    states = ["pending","pending","pending","running"]
    return random.choice(states)

instance_state = "pending"
attempts = 0

while instance_state != "running" and attempts < 5:
    print(f"Attempt {attempts + 1}:Instance state is {instance_state}")
    instance_state = stimulate_instance_state ()
    attempts += 1
    time.sleep(1) # Wait for 1 second between checks

if instance_state == "running":
    print("Instancde is now running!")
else:
    print("Instance did not start in time.")