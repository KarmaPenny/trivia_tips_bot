from groupme import GroupMe
import secrets 
from twitter import Twitter


def main(event, context):
  # load config from Amazon SecretsManager
  config = secrets.load("tomato_jakes_trivia_bot_secrets")

  # get latest tips from Sparky's twitter
  twitter = Twitter(config.twitter_access_token)
  tips = twitter.get_latest_tweet("from:SparkyMacMillan trivia tip")

  # post tips to groupme
  if tips:
    groupme = GroupMe(config.groupme_access_token)
    groupme.post(config.groupme_bot_id, tips)
