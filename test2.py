import boto3
AWS_ACCESS_KEY_ID = 'AKIAQVXMC4NI7ELF6VX7'
AWS_SECRET_ACCESS_KEY = '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'
session=boto3.session(profile_name="aws_ec2_iam_user",region_name='us-east-1')
ec2_re_ob=session.resource(service_name="ec2")

for each_instance in ec2_re_ob.instances.all():
    print(each_instance)
