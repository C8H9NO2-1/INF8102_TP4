import boto3

client = boto3.client('cloudformation')

response = client.create_stack(
    StackName='s3-stack-2-backup',
    TemplateURL='https://polystudents3-460783431840.s3.ca-central-1.amazonaws.com/s3-2-backup.json',
    Parameters=[
    ],
    DisableRollback=True,
    EnableTerminationProtection=False,
    RetainExceptOnCreate=True
)
