import tweepy
from secrets import secrets

# Authenticate to Twitter
auth = tweepy.OAuthHandler(secrets['api_key'], secrets["api_secret_key"])
auth.set_access_token(secrets["access_token"], secrets["access_token_secret"])
# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# api.update_status("Test tweet from Tweepy Python -- poetry-bot")

