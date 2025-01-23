# Single qoutes
single_quotes = 'This is an EC2'

# Double quotes
double_quote = 'This is an S3 bucket'

# Triple quotes for multi-line strings
multi_line = """ 
This is a Cloudformation template.
Which had multiple lines
"""

print(single_quotes)
print(double_quote)
print(multi_line)


# Exercise

aws_region = 'us-west-2'
ec2_instance_type = "t3.micro"
iam_policy = """
{
    "Version": "2012-10-17
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3::example-bucket"
        }
    ]
}
"""
# Exercise 
print(aws_region) 
print(ec2_instance_type)
print(iam_policy)