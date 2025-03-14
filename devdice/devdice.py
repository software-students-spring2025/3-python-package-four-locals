import random

class Eliminator:
    # need to initialize an eliminator object that we pass in our list of items to
    def __init__(self, items):
        self.items = list(items)

    # function that we call to make the eliminations.
    # returns the eliminated item.
    def eliminate(self):
        if not self.items:
            raise ValueError("No more items to eliminate!")
        return self.items.pop(random.randint(0, len(self.items) - 1))
    
# a new take on roulette, where the chances of winning increase each time
def roulette(slots=6, starting=1):
    if not hasattr(roulette, "extra"):
        roulette.extra = 0

    roulette.extra += 1
    return random.randint(1, slots) <= (starting + roulette.extra)

# def roulette(slots=6, starting=1):
#     if not hasattr(roulette, "extra"):
#         roulette.extra = 0

#     # Adjust the chance gradually based on the extra value
#     # For example, increase the chances of winning each time
#     chance = starting + roulette.extra
#     result = random.randint(1, slots) <= chance

#     # Increase roulette.extra after each round
#     roulette.extra += 1

#     return result
