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

def flipACoin(num: int) -> list[str]:
    if num <= 0:
        raise ValueError("Number of flips must be greater than zero.")
    return [random.choice(["Heads", "Tails"]) for _ in range(num)]

def rollADice(num: int) -> list[int]:
    if num <= 0:
        raise ValueError("Number of rolls must be greater than zero.")
    return [random.randint(1, 6) for _ in range(num)]

def rockPaperScissors():
    outcomes = ['Rock', 'Paper', 'Scissors']
    return outcomes[random.randint(0, 2)]

print(rockPaperScissors())
def randomColorGenerator(num: int) -> list[str]:
    if num <= 0:
        raise ValueError("Must generate at least one color.")
    
    def colorGen():
        hex_color = ''
        for _ in range(6):
            hex_color += f"{random.randrange(0, 15):x}"
        return hex_color
    
    if num == 1:
        return colorGen()
    
    return [colorGen() for _ in range(num)]

# ============================== Chooser Class  ==============================

class Chooser:

    # Constructor
    def __init__(self, options):
    
        if not options:
            raise ValueError("Must have at least one option.")
        self.options = list(options)


    # Return a Random Choice
    def pick(self):
        return random.choice(self.options)
    

    # Add Option to Options Array
    def add_option(self, option):
        self.options.append(option)


    # Remove Option from Options Array
    def remove_option(self, option):

        if option in self.options:
            self.options.remove(option)
        else:
            raise ValueError("Option not found.")

    # Getter
    def get_options(self):
        return self.options
    
    
# ========================== Magic EightBall Class  ==========================

class MagicEightBall:

    # Constructor
    def __init__(self):
         self.responses = ["Yes, definitely!","For sure!", "100%", "I'd bet my life on it", "Yessir!", "Without a doubt.",
                            "No!", "Definitely Not!","Nahh!", "No shot", "Not a chance.", "Absolutely not.", "I don't think you want to know"
                            "Maybe", "Potentially...", "Could be",  "Most likely.", "Don't count on it.", "Very doubtful.",
                            "Prob", "Prob Not", "I think ur cooked", "That's Unfortunate"]
    

    # Returns Random Option From Response Array
    def shake(self) -> str:
        if not self.responses:
            raise ValueError("No responses in Magic 8-Ball.")
        index = random.randint(0, len(self.responses)-1)
        return self.responses[index]
    

    # Add New Response 
    def add_response(self, response: str):
        self.responses.append(response)

    
    # Remove Response
    def remove_response(self, response: str):
        if response in self.responses:
            self.responses.remove(response)
        else:
            raise ValueError("Response not found.")

    # Getter 
    def get_responses(self):
        return self.responses

    # Starts a Magic Ball Simulation
    def start_simulation(self):
        print("Welcome to the Magic 8 Ball! Type your question and press Enter.")
        print("Type 'exit' to quit.\n")
        
        while True:

            question = input("Enter your question: ").strip()
            
            if question.lower() == "exit":
                print("Goodbye! ")
                break

            if question == "":
                print("Please enter a valid question.")
            else:
                print(self.shake())
                print("\n")