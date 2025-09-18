# Design a Food Rating System
import heapq

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        # Maps food -> (cuisine, rating)
        self.food_info = {}
        
        # For each cuisine, a max-heap of (-rating, name)
        self.cuisine_map = {}
        
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = [c, r]
            if c not in self.cuisine_map:
                self.cuisine_map[c] = []
            heapq.heappush(self.cuisine_map[c], (-r, f))

    def changeRating(self, food, newRating):
        cuisine, _ = self.food_info[food]
        # Update food rating
        self.food_info[food][1] = newRating
        # Push new rating into heap
        heapq.heappush(self.cuisine_map[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        # Pop outdated items until valid top
        heap = self.cuisine_map[cuisine]
        while heap:
            rating, food = heap[0]
            # If matches current rating, return it
            if -rating == self.food_info[food][1]:
                return food
            heapq.heappop(heap)  # remove stale entry

foods     = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines  = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings   = [9, 12, 8, 15, 14, 7]

system = FoodRatings(foods, cuisines, ratings)
print(system.highestRated("korean"))   # "kimchi" (rating 9 > bulgogi 7)
print(system.highestRated("japanese")) # "ramen" (rating 14 > miso 12 > sushi 8)

system.changeRating("sushi", 16)       # update sushi rating
print(system.highestRated("japanese")) # "sushi" (rating 16 is highest)
