import tweepy

api_key = ""
api_secret_key = ""
access_token = ""
access_token_secret = ""

# Create The Authenticate Object
authenticate = tweepy.OAuthHandler(api_key, api_secret_key)

# Set The Access Token & Access Token Secret
authenticate.set_access_token(access_token, access_token_secret)

# Create The API Object
api = tweepy.API(authenticate, wait_on_rate_limit = True)

tweets = api.user_timeline(screen_name = "elonmusk", count = 5, lang = "en", tweet_mode = "extended")

for tweet in tweets:
    print(f"- {tweet.full_text}")
