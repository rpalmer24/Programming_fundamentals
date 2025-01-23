# For Loops

# for item in sequence:
    # code to execute for each item

instance_ids = ["i-123456abca", "i-23456", "i-abcde1234"]

for instance_id in instance_ids:
    print(f"Checking status of instance {instance_id}")
    # code to check instance status
    print(f"instance {instance_id} status check complete")

print("All instances have been checked")