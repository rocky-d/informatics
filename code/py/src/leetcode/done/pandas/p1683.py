from leetcode.util import *


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[15 < tweets['content'].str.len()][['tweet_id']]
