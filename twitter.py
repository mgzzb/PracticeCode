class Twitter:

    def __init__(self):
        self.time = 0  # track tweet order
        self.tweets = {}  # Maps userId with list including (time, tweetId)
        self.following = {}  # Maps userId with set of userIds they follow

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []

        users = self.following.get(userId, set())

        if userId not in users:
            users.add(userId)
        
        for follow in users:
            news.extend(self.tweets.get(follow, []))

        news.sort(reverse=True, key=lambda x:x[0])

        return [id_tweet for _, id_tweet in news[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
