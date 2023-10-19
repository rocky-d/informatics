from leetcode.util import *


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[['tweet_id']][15 < tweets['content'].str.len()]
