from flask import Flask, request, jsonify
import tweepy

app = Flask(__name__)

API_key = "iQPitmVYBJnS9vcIuK639vEUI"
API_secret_key = "DemHcohNOJxWE22hAWOVY2wrwykOyZtOCVl2zt9Y5la1tZRxyD"
access_token="293390592-LPZDqfqzqVWknb1XfQG0yXnbZL7bFCOhXRMW5dex"
access_token_secret =   "Pp9SnxoiVuncgpAJ7RHY804aJgT0fiDiHwNPQQxSBT9Xo"

QTYPE = {
    'users': '@',
    'hashtags': '#',
    #add more ..
}

def search_tweets(query, limit):
    """
    To search tweets for given query parameter
    """
    tweets = []
    auth = tweepy.OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    try:
        cursor = tweepy.Cursor(api.search, q=query, count=limit).items()
        while limit>0:
            limit -= 1
            tweets.append(cursor.next()._json)
    except:
        pass
    return tweets

def user_tweets(query, limit):
    """
    To get user timelin tweets for given userid
    FIXME dedup the common code lines
    """
    tweets = []
    auth = tweepy.OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    try:
        cursor = tweepy.Cursor(api.user_timeline, screen_name=query, count=limit).items()
        while limit>0:
            limit -= 1
            tweets.append(cursor.next()._json)
    except:
        pass
    return tweets

@app.route('/hashtags/<string:query>/')
def hashtags(query):
    limit = request.args.get('limit', default=30, type=int)
    tweets = search_tweets("#%s" % query, limit)
    return jsonify(tweets)

@app.route('/user/<string:query>/')
def users(query):
    limit = request.args.get('limit', default=30, type=int)
    # tweets = user_tweets(query, limit)
    tweets = search_tweets("@%s" % query, limit)
    return jsonify(tweets)

if _name_ == '__main__':
    app.run(debug=True)