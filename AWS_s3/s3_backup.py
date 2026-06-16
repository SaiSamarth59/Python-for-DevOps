import boto3

s3=boto3.resource("s3")
def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)
def create_bucket(s3):
    s3.create_bucket(Bucket="python-for-devops-59",
                     CreateBucketConfiguration={
                     'LocationConstraint': 'us-east-2',    
                     },)
    print("Bucket created successfully")

create_bucket(s3)
show_buckets(s3)