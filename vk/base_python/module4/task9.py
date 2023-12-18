from typing import List


class Twitter:
    def __init__(self):
        self.followees = {}
        self.users_tweets = {}
        self.tweet_counter = 0

    def post_tweet(self, user_id, tweet_id):
        self.tweet_counter += 1
        try:
            self.users_tweets[user_id].append((tweet_id, self.tweet_counter))
        except KeyError:
            self.users_tweets[user_id] = [(tweet_id, self.tweet_counter)]

    def get_news_feed(self, user_id) -> List[int]:
        news_feed = []
        for sub in self.followees[user_id]:
            news_feed.extend(self.users_tweets[sub])
        sorted_news_feed = sorted(news_feed, key=lambda x: x[1], reverse=True)

        return [el[0] for el in sorted_news_feed][:10]

    def follow(self, follower_id, followee_id):
        try:
            self.followees[follower_id].append(followee_id)
        except KeyError:
            self.followees[follower_id] = [followee_id]

    def unfollow(self, follower_id, followee_id):
        try:
            self.followees[follower_id].remove(followee_id)
        except KeyError:
            pass
        except ValueError:
            pass


# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)
