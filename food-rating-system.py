import heapq

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            if cuisine not in self.cuisine_to_heap:
                self.cuisine_to_heap[cuisine] = []
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        # Push new rating into heap
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_to_heap[cuisine]
        # Lazy removal of outdated ratings
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)  # remove outdated entry

