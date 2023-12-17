from rockyutil.leetcode import *


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.menu = dict()
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.menu[cuisine] = self.menu.get(cuisine, {}) | {food: rating}

    def changeRating(self, food: str, newRating: int) -> None:
        for cuisine in self.menu.keys():
            if food in self.menu[cuisine].keys():
                self.menu[cuisine][food] = newRating
                break

    def highestRated(self, cuisine: str) -> str:
        return sorted(tuple(self.menu[cuisine].items()), key = lambda item: (-item[1], item[0]))[0][0]
