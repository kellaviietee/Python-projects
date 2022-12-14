"""Twitter."""
import re


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old and has 64 retweets.
    >Tweet2 is 3.12 hours old and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """
    fastest_tweet_list = sorted(tweets, key=lambda x: find_the_growth_of_tweet(x.retweets, x.time), reverse=True)
    return fastest_tweet_list[0]


def find_the_growth_of_tweet(number_of_retweets: int, how_long_to_retweet: int) -> float:
    """
    Find the growth rate of a tweet.

    :param number_of_retweets: How many times has it been retweeted.
    :param how_long_to_retweet: How long it took to reach that number of retweets
    :return: Rate of growth of those retweets.
    """
    return number_of_retweets / how_long_to_retweet


def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.

    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    popular_tweets = sorted(tweets, key=lambda x: (x.retweets, -x.time), reverse=True)
    return popular_tweets


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    tweets_with_hastag = []
    for tweet in tweets:
        if hashtag in tweet.content:
            tweets_with_hastag.append(tweet)
    return tweets_with_hastag


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    all_hashtags = {}
    for tweet in tweets:
        match = re.findall(r"#\w+", tweet.content)
        for hashtag in match:
            if hashtag not in all_hashtags:
                all_hashtags[hashtag] = tweet.retweets
            else:
                all_hashtags[hashtag] += tweet.retweets
    this_is_dummy = all_hashtags.copy()
    hashtag_popularity = sorted(all_hashtags, key=lambda x: (this_is_dummy[x], x), reverse=True)
    return hashtag_popularity


def sorting_hashtag(all_hashtags_dict: dict, key: str) -> int:
    """
    Sort hashtags by their popularity.

    :param all_hashtags_dict: Dictionary of all hashtags.
    :param key:
    :return:
    """
    return all_hashtags_dict[key]


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3]

    print(filter_by_hashtag(tweets, "#heart"))
