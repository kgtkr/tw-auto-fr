import os
import tweepy
import time
from dotenv import load_dotenv

load_dotenv(".env")


# 環境変数取得
ck = os.environ["ck"]
cs = os.environ["cs"]
tk = os.environ["tk"]
ts = os.environ["ts"]

# 認証
auth = tweepy.OAuthHandler(ck, cs)
auth.set_access_token(tk, ts)
api = tweepy.API(auth)

while True:
    try:
        for id in api.friendships_incoming():
            tweepy.binder.bind_api(api=api,
                                   method='POST',
                                   path='/friendships/accept.json',
                                   payload_type='user',
                                   allowed_param=['user_id'])(user_id=id)
        time.sleep(60*3)
    except Exception as e:
        print(e)
