Twitter content extraction API

Description:
The API provide tweets content based on hash tag and user based.

1. Get tweets by a hashtag. Get the list of tweets with the given hashtag.
Optional parameters: limit: integer, specifies the number of tweets to retrieve, default should be 30
example: http://localhost:8000/hashtags/python/?limit=10

2. Get user tweets. Get the list of tweets that user has on his feed in json format. Optional parameters: 
limit: integer, specifies the number of users to retrieve, default should be 30
example: http://localhost:8000/user/kannan/?limit=10

Requirements:
Use below command to install requirements packages.
pip install -r requirements.txt

required packages:
certifi==2018.8.24
chardet==3.0.4
click==6.7
Flask==1.0.2
idna==2.7
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
oauthlib==2.1.0
PySocks==1.6.8
requests==2.19.1
requests-oauthlib==1.0.0
six==1.11.0
tweepy==3.6.0
urllib3==1.23
Werkzeug==0.14.1

Create Twitter Developer Account:
  1. Create developer account in twitter.
      https://developer.twitter.com/
      
  2. Create your application in twitter and get API key and configure in app.py like below
     API_key = "iQPitmVYBJnS9vcIuK639vEUI" <your api key>
     API_secret_key = "DemHcohNOJxWE22hAWOVY2wrwykOyZtOCVl2zt9Y5la1tZRxyD" <your api secret key>
     access_token="293390592-LPZDqfqzqVWknb1XfQG0yXnbZL7bFCOhXRMW5dex" <your access token>
     access_token_secret =   "Pp9SnxoiVuncgpAJ7RHY804aJgT0fiDiHwNPQQxSBT9Xo" < your access token secret>
 
Running Project:
  python app.py
