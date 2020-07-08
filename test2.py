import boto3
AWS_ACCESS_KEY_ID = 'xxxxxxxxxxxxxxxxxxxxxx'
AWS_SECRET_ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
session=boto3.session(profile_name="aws_ec2_iam_user",region_name='us-east-1')
ec2_re_ob=session.resource(service_name="ec2")

for each_instance in ec2_re_ob.instances.all():
    print(each_instance)
