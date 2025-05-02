import praw
from praw.models import Submission
import pandas as pd
import time

df = pd.read_csv("back_end/csvfiles/processeddata.csv", header=None, index_col = None)

reddit = praw.Reddit(

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
