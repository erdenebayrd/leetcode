from collections import OrderedDict

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.auths = OrderedDict()
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.auths[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.auths:
            return
        if self.auths[tokenId] <= currentTime:
            del self.auths[tokenId]
            return
        self.auths[tokenId] = currentTime + self.ttl
        self.auths.move_to_end(tokenId, last=True)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while len(self.auths) > 0 and self.auths[next(iter(self.auths))] <= currentTime:
            del self.auths[next(iter(self.auths))]
        # print(self.auths)
        return len(self.auths)

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)