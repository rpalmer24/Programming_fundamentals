# Define the AWS account ID
account_id = "12345678012"

# Define the project name
projecct_name = "cloud_project"

# Concatenate strings to form the S3 bucket name
bucket_name = account_id + '_' + projecct_name + "-bucket"

# Print the resulting bucket name
print(f"S3 Bucket Name: {bucket_name}")


# Excercise EC2 String Concatenation

# Environment name prod, dev, staging
environment = "dev"
# application name
application = "appserver"
# instance number
instance_id = "369"
# Concatenate
instance_name = environment + '-' + application + "-instance-" + instance_id

# Print
print(f"EC2 Instance name:" + instance_name)