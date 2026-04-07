class Fancy:

    def __init__(self):
        # a * x + b
        self.values = [0]
        self.multiplies = [1]
        self.addies = [0]
        self.mod = 1_000_000_007

    def append(self, val: int) -> None:
        self.values.append(val)
        self.multiplies.append(self.multiplies[-1])
        self.addies.append(self.addies[-1])

    def addAll(self, inc: int) -> None:
        self.addies[-1] = (self.addies[-1] + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.multiplies[-1] = (self.multiplies[-1] * m) % self.mod
        self.addies[-1] = (self.addies[-1] * m) % self.mod

    def getIndex(self, idx: int) -> int:
        idx += 1
        if idx >= len(self.values):
            return -1
        # multiply = (self.multiplies[-1] / self.multiplies[idx - 1]) % self.mod
        # (a / b) % mod => (a % mod) * (b^-1) % mod) % mod
        # (b^-1) % mod
        # (b ^ -1) % mod => (b ^ (mod - 2)) % mod 
        # in terms of ferma's little theorom
        # x ^ (p - 1) = 1 (p is prime number)
        # both sides divided by x
        # x ^ (p - 2) = x ^ -1
        # meaning => b ^ (-1) = (b ^ (mod - 2)) % mod
        inverse = pow(self.multiplies[idx - 1], self.mod - 2, self.mod)
        multiply = (self.multiplies[-1] * inverse) % self.mod
        addie = (self.addies[-1] - self.addies[idx - 1] * multiply) % self.mod
        value = (self.values[idx] * multiply + addie) % self.mod
        return value


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)