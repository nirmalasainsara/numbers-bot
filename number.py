import os
import tweepy
import requests
import random

API_KEY = os.environ.get("API_KEY")
API_KEY_SECRET = os.environ.get("API_KEY_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

url = "http://numbersapi.com/random/"
addon_choices = ["math", "year", "date", "trivia"]


def get_request():
    addon_url = random.choice(addon_choices)
    # make get request
    response = requests.get(url + addon_url)
    tweet = response.text
    return tweet


def authenticate():
    # Handle tweepy auntentication
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    return api


def send_response(api, tweet):
    # Upload random tweet
    status = api.update_status(tweet)


if __name__ == "__main__":
    tweet = get_request()
    api = authenticate()
    send_response(api, tweet)
