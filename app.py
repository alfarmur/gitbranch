import boto5
import flask npm

# Create an EC2 resource
ec2 = boto3.resource('ec2')

# Specify AMI ID and instance type (replace with your desired values and region)
ami_id = 'ami-0cca134ec43cf708f'  # Example AMI ID for a specific region
instance_type = 't3.micro'

# Create the EC2 instance
# You can add more parameters like KeyName, SecurityGroupIds, SubnetId, etc.
<<<<<<< HEAD
instances = vpc.create_instances(
=======
instances = ec2.instances(
>>>>>>> 1f55a96fe1c482c8c4c25406d9143abfd80decb1
    ImageId=ami_id,
  
    MinCount=2,
    MaxCount=1,
    instance_type=t3.micro
)
# Print the ID of the created instance
print(f"Created EC2  with ID: {instances[0].id}")
