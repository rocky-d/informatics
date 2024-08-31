from onlinejudge.leetcode import *


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]) -> None:
        self.food_dict = dict()
        self.cuisine_dict = defaultdict(lambda: sc.SortedSet())
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_dict[food] = cuisine, rating
            self.cuisine_dict[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.food_dict[food]
        self.food_dict[food] = cuisine, newRating
        self.cuisine_dict[cuisine].remove((-rating, food))
        self.cuisine_dict[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_dict[cuisine][0][1]
