class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.n = len(foods)
        self.foodTypes = {}
        self.groups = {}
        self.rating = {}
        for i in range(self.n):
            self.foodTypes[foods[i]] = cuisines[i]
            if cuisines[i] not in self.groups:
                self.groups[cuisines[i]] = SortedList([])
            self.groups[cuisines[i]].add([-ratings[i], foods[i]])
            self.rating[foods[i]] = -ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        currentFoodType = self.foodTypes[food]
        currentRating = self.rating[food]
        self.groups[currentFoodType].remove([currentRating, food])
        self.rating[food] = -newRating
        self.groups[currentFoodType].add([-newRating, food])

    def highestRated(self, cuisine: str) -> str:
        # print(cuisine)
        # print(self.groups)
        # print("-" * 10)
        return self.groups[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)