import requests
from email_send import email_sender    

api_key="f3eb410c821e43c6a632c6a7383c1bbc"
url="https://newsapi.org/v2/everything?q=tesla&from=2024-06-15&sortBy=publishedAt&apiKey=f3eb410c821e43c6a632c6a7383c1bbc"

req=requests.get(url)
content=req.json()
content["articles"]

for article in content["articles"]:
    if article['title'] is not None:
        title=article['title']
        description=article['description']
        message=""
        message=message+'\n'+'\n'+title+'\n'+description
    
message=message.encode('utf-8')
email_sender(message)
