class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.d = defaultdict(set)
        self.c = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.c, tweetId))
        self.c -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if userId not in self.d[userId]:
            self.d[userId].add(userId)

        for following in self.d[userId]:
            if self.tweets[following]:
                idx = len(self.tweets[following]) - 1
                time, tweetId = self.tweets[following][idx]
                heapq.heappush(heap, (time, tweetId, following, idx))
        
        res = []
        while heap and len(res) < 10:
            time, tweetId, followId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx > 0:
                idx -= 1
                nTime, ntweetId = self.tweets[followId][idx]
                heapq.heappush(heap, (nTime, ntweetId, followId, idx))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.d[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:   
        self.d[followerId].discard(followeeId)
