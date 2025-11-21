import boto3

client = boto3.client('cloudformation')

response = client.create_stack(
    StackName='polystudent-stack-2',
    TemplateURL='https://polystudents3-460783431840.s3.ca-central-1.amazonaws.com/vpc.yaml',
    Parameters=[
        {
            'ParameterKey': 'EnvironmentName',
            'ParameterValue': 'Lab2',
        },
    ],
    DisableRollback=True,
    EnableTerminationProtection=False,
    RetainExceptOnCreate=True
)
