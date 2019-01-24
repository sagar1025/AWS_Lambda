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
`chalice deploy --no-autogen-policy`  

#### By default the name of the project and the API that is set up is called sent, and the environment to which it is deployed is called dev

###### This API takes json requests and returns a json that contains news articles that are "Neutral" as determined by Comprehend  

### Sample request  
`
{
"articles": [
{
	"title": "homes got fancier this year at CES",
"description": "The smart home market is still up for grabs Unlike PCs or phones, which for the most part are dominated by a few well known names  smart home gadgets can come from wherever and whatever brand  As long as they perform functions you cant get from the big na",
"content": "The smart home market is still up for grabs. Unlike PCs or phones which for the most part are dominated by a few well known names smart home gadgets can come from wherever and whatever brand As long as they perform functions you cant get from the big nam"
},
{
	"title": "Netflix sued by Choose Your Own Adventure publishers over Black Mirror: Bandersnatch",
"description": "Chooseco, publisher of the Choose Your Own Adventure series, has filed a trademark infringement lawsuit against Netflix for referencing its books in the interactive Black Mirror episode Bandersnatch."
},
{
	"title": "Polished Putin, tempestuous Trump are a contrast in foreign policy styles",
"description": "Last years Helsinki summit still seems to be paying dividends for Russian President Vladimir Putin."
}
]}
`  
### Response  
`
{
    "0": {
        "content": "The smart home market is still up for grabs. Unlike PCs or phones which for the most part are dominated by a few well known names smart home gadgets can come from wherever and whatever brand As long as they perform functions you cant get from the big nam",
        "description": "The smart home market is still up for grabs Unlike PCs or phones, which for the most part are dominated by a few well known names  smart home gadgets can come from wherever and whatever brand  As long as they perform functions you cant get from the big na",
        "title": "homes got fancier this year at CES"
    },
    "1": {
        "description": "Chooseco, publisher of the Choose Your Own Adventure series, has filed a trademark infringement lawsuit against Netflix for referencing its books in the interactive Black Mirror episode Bandersnatch.",
        "title": "Netflix sued by Choose Your Own Adventure publishers over Black Mirror: Bandersnatch"
    },
    "2": {
        "description": "Last years Helsinki summit still seems to be paying dividends for Russian President Vladimir Putin.",
        "title": "Polished Putin, tempestuous Trump are a contrast in foreign policy styles"
    }
}
`
