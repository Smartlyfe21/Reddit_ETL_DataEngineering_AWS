from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH
import pandas as pd
import os
from datetime import datetime


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    """
    Extract posts from Reddit, transform, and save to CSV.
    """

    # Connect to Reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'AirScholar Agent')

    # Extract posts
    posts = extract_posts(instance, subreddit, time_filter, limit)

    # Select fields for modeling
    post_data = []
    for post in posts:
        post_data.append({
            'id': post.id,
            'title': post.title,
            'score': post.score,
            'num_comments': post.num_comments,
            'author': str(post.author),
            'subreddit': str(post.subreddit),
            'created_utc': datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
            'url': post.url
        })

    # Create DataFrame
    post_df = pd.DataFrame(post_data)

    # Optional: Transform data
    post_df = transform_data(post_df)

    # Ensure output folder exists
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    # Load to CSV
    file_path = os.path.join(OUTPUT_PATH, f'{file_name}.csv')
    load_data_to_csv(post_df, file_path)

    return file_path
