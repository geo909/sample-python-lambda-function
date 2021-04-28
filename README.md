#### Instructions

* Install docker and start the service
* Install and configure [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* To test the function locally:
  - `sam build --use-container`
  - `sam local invoke test4stefanos --profile ferryhopper --region eu-west-2 --event events/event.json`
  The region parameter may not be needed, depending on the aws cli configuration
* Deploy with `sam deploy --guided` for the first time, and just `sam deploy` every subsequent time



#### Random notes

* The S3 bucket, lambda function and any lambda layers should be in the same region
