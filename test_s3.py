import random

def create_s3_bucket(bucket_name):
    random_number = random.randint(888,9999)
    bucket_name = f"{bucket_name}-bucket-{random_number}"
    return bucket_name

new_bucket = create_s3_bucket("Project")
print(f"Created new S3 bucket:{new_bucket}")
