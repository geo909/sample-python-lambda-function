import json
import os

def lambda_handler(event, context):
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda2!')
    }


if __name__ == "__main__":

    print('Hello there from lambda2')
