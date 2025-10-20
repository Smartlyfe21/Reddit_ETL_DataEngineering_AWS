import sys
import numpy as np
import pandas as pd
import praw
from praw import Reddit
from typing import List, Dict


# Define the fields to extract from Reddit posts
POST_FIELDS = [
    'id', 'title', 'selftext', 'author', 'created_utc',
    'score', 'num_comments', 'over_18', 'subreddit'
]

def connect_reddit(client_id: str, client_secret: str, user_agent: str) -> Reddit:
    """Connect to Reddit API using PRAW and return a Reddit instance."""
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        print("Connected to Reddit!")
        return reddit
    except Exception as e:
        print(f"Error connecting to Reddit: {e}")
        sys.exit(1)


def extract_posts(
    reddit_instance: Reddit,
    subreddit: str,
    time_filter: str = 'day',
    limit: int = None
) -> List[Dict]:
    """Extract top posts from a subreddit."""
    subreddit_obj = reddit_instance.subreddit(subreddit)
    posts = subreddit_obj.top(time_filter=time_filter, limit=limit)

    posts_list = []
    for post in posts:
        post_dict = vars(post)
        filtered_post = {key: post_dict.get(key) for key in POST_FIELDS}
        posts_list.append(filtered_post)

    return posts_list


def transform_data(post_df: pd.DataFrame) -> pd.DataFrame:
    """Transform the Reddit post data."""
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    post_df['over_18'] = post_df['over_18'].astype(bool)
    post_df['author'] = post_df['author'].astype(str)
    edited_mode = post_df['author'].astype(str)
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]),
                                 post_df['edited'], edited_mode).astype(bool)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['upvote_ratio'] = post_df['upvote_ratio'].astype(int)
    post_df['selftext'] = post_df['selftext'].astype(str)
    post_df['title'] = post_df['title'].astype(str)

    return post_df


def load_data_to_csv(data: pd.DataFrame, path: str):
    """Save the DataFrame to CSV."""
    data.to_csv(path, index=False)
    print(f"Data saved to {path}")
