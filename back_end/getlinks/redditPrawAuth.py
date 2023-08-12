import praw
import pandas as pd
from validate_links import isValidPost

reddit = praw.Reddit(
    client_id="sFrh8LTFghvT1hTi1_fuBg",
    client_secret="Z9lv8U8J08iE07o3s-xxzvMevoaV2Q",
    user_agent="collegeresults",
)

posts = []

college_results_subreddit = reddit.subreddit("collegeresults")

for post in college_results_subreddit.new(limit= None):
    if (post.created_utc < 1681261200):
        break
    condition = isValidPost(f"https://www.reddit.com/r/collegeresults/comments/{post.id}")
    if (condition):
        posts.append(f"https://www.reddit.com/r/collegeresults/comments/{post.id}")

df = pd.DataFrame(posts, index = None).to_csv("../csvfiles/newfilteredlinks.csv", header = None)







