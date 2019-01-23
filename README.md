# AWS Lambda function/serverless API that uses Comprehend API

### Dependencies
<a href="https://github.com/aws/chalice" target="_blank">Chalice</a>  
<a href="https://github.com/boto/boto3" target="_blank">Boto3</a>  


### Set up Chalice
`chalice new-project sent`  
### To run on localhost  
`chalice local`  
this will run on localhost  
### To deploy   
`chalice deploy`  

#### By default the name of the project and the API that is set up is called sent, and the environment to which it is deployed is called dev

###### This API takes json requests and returns a json that contains news articles that are "Neutral" as determined by Comprehend