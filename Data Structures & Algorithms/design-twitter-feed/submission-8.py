class Twitter:

    def __init__(self):
        self.recentHeap = []
        self.followerMap = {}
        self.tweetCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.recentHeap, [self.tweetCount, userId, tweetId])
        self.tweetCount -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followed = self.followerMap[userId].copy() if userId in self.followerMap else []
        followed.append(userId)
        newHeap = []
        res = []
        while self.recentHeap and len(res) < 10:
            top = heapq.heappop(self.recentHeap)
            if top[1] in followed:
                res.append(top[2])
        
            newHeap.append(top)
        
        for item in newHeap:
            heapq.heappush(self.recentHeap, item)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followerMap:
            self.followerMap[followerId] = [followeeId]
        else:
            self.followerMap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        while followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
