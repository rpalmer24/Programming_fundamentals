# List of EC2 instance
instance_ids = ["i-1234","i-5678","i-9012"]

# List of IP addresses for a secuirty group
ip_addresses = ["10.0.0.1","10.0.0.2","10.0.0.3","10.0.0.4"]

# List of availability zones in a region
availability_zones = ["eu-west-1a","eu-west-2a","eu-west-2c"]

# Print the lists
#print(f"EC2 Instances to terminate: {instance_ids}")
#print(f"IP Addresses to terminate: {ip_addresses}")
print(f"Availability Zone to terminate: {availability_zones}")

#Add new EC2 Instance ID
#instance_ids.append("i-3456")
#print("After adding a new instance ID")
#print("EC2 Insances:", instance_ids)

# Remove EC2 Instance ID
#instance_ids.remove("i-1234")
#print("After removing the instance ID")
#print("EC2 Instances:", instance_ids)

# Check if item is in the list
#if "10.0.0.4" in ip_addresses:
#    print("Yes 10.0.0.4 is in and allowed")
#else:
#    print("No 10.0.0.4 is not the allowed list")
#print("IP addresses:", ip_addresses)


# Slicing a List
# First two AZ

first_two_azs = availability_zones[:1]
print("First two AZs", first_two_azs)

# Sorting
instance_ids.sort()
#print("Sorted EC2 Instance", instance_ids)

# Finding lenght of a list
number_of_ips = len(ip_addresses)
#print(f"Number of IP addresses: {number_of_ips}")
#print(first_two_azs)

# Accessing list of items by index
first_az= availability_zones [0]
last_az =availability_zones [-1]
print(f"First Az:", first_az)
print(f"Last AZ:",last_az)