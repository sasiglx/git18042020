import boto3  
access_key = "AKIAQVXMC4NI7ELF6VX7"
secret_key = "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"

client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name='us-east-1')


#ec2client = boto3.client('ec2')
response = client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        #print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        print(instance["InstanceId"], instance["InstanceType"])