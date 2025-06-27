import boto3

# Create an EC2 resource
ec2 = boto3.resource('ec2')

# Specify AMI ID and instance type (replace with your desired values and region)
ami_id = 'ami-0cca134ec43cf708f'  # Example AMI ID for a specific region
instance_type = 't2.micro'

# Create the EC2 instance
# You can add more parameters like KeyName, SecurityGroupIds, SubnetId, etc.
instances = ec2.create_instances(
    ImageId=ami_id,
    MinCount=1,
    MaxCount=2,
    InstanceType=instance_type
)

# Print the ID of the created instance
print(f"Created EC2 instance with ID: {instances[0].id}")
