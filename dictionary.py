# Dictionaries
# - Store and retrieve information
# - Key and Values

# EC2

ec2_instance = {
    "InstanceId": "i-123456abcde",
    "InstanceType": "t2.micro",
    "State": "running",
    "PublicIpAddress": "203.0.111.2"
}

instance_id = ec2_instance["InstanceId"]
print(f"this is a  {instance_id} instance")

# if we are not sure a key exists
public_ip = ec2_instance.get("PublicIpAddress", "No Public IP address is here")
print(f"the instance public ip is: {public_ip}")

# Adding a new key-value pair
ec2_instance["AvailabilityZone"] = "eu-west-2"
ec2_instance["State"] = "stopped"

print(ec2_instance)

# To Remove Resources
# Using pop () removes the key value pair and returns the value
rm_instance_type = ec2_instance.pop("InstanceType")
print (f"removed instance type: {rm_instance_type}")
print(ec2_instance)

# Using Del simply removing the key value pair but does not return the value
del ec2_instance["AvailabilityZone"]
print(ec2_instance)