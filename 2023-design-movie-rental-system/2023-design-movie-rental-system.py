from sortedcontainers import SortedList

class MovieRentingSystem:

    # time: O(N Log N)
    # space: O(N)
    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(SortedList)
        self.rented = SortedList([])
        self.prices = defaultdict(lambda: defaultdict(int))
        for shop, movie, price in entries:
            self.prices[shop][movie] = price
            self.movies[movie].add([price, shop])

    def search(self, movie: int) -> List[int]:
        return [shop for _, shop in self.movies[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[shop][movie]
        self.movies[movie].remove([price, shop])
        self.rented.add([price, shop, movie])

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[shop][movie]
        self.rented.remove([price, shop, movie])
        self.movies[movie].add([price, shop])

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()