import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key= config['twitter']['api_key']
api_key_secret= config['twitter']['api_key_secret']

access_token= config['twitter']['access_token']
access_token_secret= config['twitter']['access_token_secret']


print(api_key)

#authentication(authenticate our account from twitter API)
auth=tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

#make an API instant use to access twitter account we an use it for tweet/public tweets or delete a tweet
api=tweepy.API(auth)
#user tweets
user="veritasium"
limit=30
tweets=api.user_timeline(screen_name=user,count=limit)
for tweet in tweets:
    print(tweet.full_text)

columns=["User","Tweet"]
data =[]
for tweet in tweets:
    data.append([tweet.user.screen_name,tweet.full_text])
print(data)

df=pd.DataFrame(data,columns=columns)
print(df)
