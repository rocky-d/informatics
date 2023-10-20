from rockyutil.leetcode import *


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.loc[15 < tweets['content'].str.len(), ['tweet_id']]
