import json
import os

'''
We will delete this lambda function soon
'''

def lambda_handler(event, context):
    
    # Accessing the event
    foo = event['Records'][0]['s3']['object']['key']
    print(foo)
    # Here you could access the bucket name and file key (i.e. its path)

    # Accessing environmental variables
    my_var = os.environ.get('MY_VAR')
    print('Env. variable is: ', my_var)

    # Process files from S3
    # boto3: get the file via its key -> process -> some result
    # result -> (python client) -> graph db
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == "__main__":

    print('You can also invoke things here for testing')
    # lambda_handler(some_test_event_here, None)
