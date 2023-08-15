import praw
from praw.models import Submission
import pandas as pd
import time

df = pd.read_csv("back_end/csvfiles/processeddata.csv", header=None, index_col = None)

reddit = praw.Reddit(
    client_id="sFrh8LTFghvT1hTi1_fuBg",
    client_secret="Z9lv8U8J08iE07o3s-xxzvMevoaV2Q",
    user_agent="redditcollegeresults.com (by /u/Dinhbaon)",
    username="Dinhbaon",
    password="Kimthanh142!?",
    ratelimit_seconds=300
)

urllist = df.iloc[:, 8].to_list()

timestamps = []

for url in urllist:

    post = Submission(reddit, url = url)

    time_created = None 
    while time_created is None:
        try:
            time.sleep(0.5)
            # connect
            time_created = post.created_utc
        except:
            time.sleep(1)
            pass

    timestamps.append(time_created)

    print(url)

df[len(df.columns)] = timestamps

df.to_csv("back_end/csvfiles/processeddata.csv", header=None, index = None)

print(df)