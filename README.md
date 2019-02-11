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
[  
   {  
      "articleTitle":"Game of Thrones Ser Davos Actor Liam Cunningham Says Season 8 Is an Honorable Ending   IGN",
      "description":"Game of Thrones actor Liam Cunningham reflects on the final season at the TCA winter press tour",
      "content":"The final season is almost here... \r\nBy David GriffinWith the highly-anticipated final season of HBO's Game of Throne fast approaching, Davos Seaworth actor Liam Cunningham spoke with IGN at the TCA winter press tour about the decision to end the series after… ",
      "articleUrl":"https://www.ign.com/articles/2019/02/11/game-of-thrones-ser-davos-actor-liam-cunningham-says-season-8-is-an-honorable-ending?abthid=5c60d5e73739c3747d001138",
      "author":"David Griffin",
      "urlToImage":"https://assets1.ignimgs.com/2019/02/11/serdavos-1549845420952_1280w.jpg"
   },
   {  
      "articleTitle":"Tips and Tricks  Tom Clancys The Division 2 Wiki Guide  IGN",
      "description":"Tom Clancys The Division 2 at IGN walkthroughs items maps video tips and strategies",
      "content":"IGN has the tips and tricks, strategies, and secrets you need to succeed in Tom Clancy's The Division 2.",
      "articleUrl":"https://www.ign.com/wikis/the-division-2/Tips_and_Tricks",
      "author":null,
      "urlToImage":"https://oystatic.ignimgs.com/src/core/img/widgets/global/page/ign-logo-100x100.jpg"
   }
]
`  
### Response  
`
[
    {
        "description": "Game of Thrones actor Liam Cunningham reflects on the final season at the TCA winter press tour",
        "author": "David Griffin",
        "content": "The final season is almost here... \r\nBy David GriffinWith the highly-anticipated final season of HBO's Game of Throne fast approaching, Davos Seaworth actor Liam Cunningham spoke with IGN at the TCA winter press tour about the decision to end the series after… ",
        "urlToImage": "https://assets1.ignimgs.com/2019/02/11/serdavos-1549845420952_1280w.jpg",
        "articleTitle": "Game of Thrones Ser Davos Actor Liam Cunningham Says Season 8 Is an Honorable Ending   IGN",
        "articleUrl": "https://www.ign.com/articles/2019/02/11/game-of-thrones-ser-davos-actor-liam-cunningham-says-season-8-is-an-honorable-ending?abthid=5c60d5e73739c3747d001138"
    },
    {
        "description": "Tom Clancys The Division 2 at IGN walkthroughs items maps video tips and strategies",
        "author": null,
        "content": "IGN has the tips and tricks, strategies, and secrets you need to succeed in Tom Clancy's The Division 2.",
        "urlToImage": "https://oystatic.ignimgs.com/src/core/img/widgets/global/page/ign-logo-100x100.jpg",
        "articleTitle": "Tips and Tricks  Tom Clancys The Division 2 Wiki Guide  IGN",
        "articleUrl": "https://www.ign.com/wikis/the-division-2/Tips_and_Tricks"
    }
]
`
