import random

# Class for an Elemination funtion
class Eliminator:
    # Constructor
    def __init__(self, items):
        if len(items) < 2:
            raise ValueError("Must have at least two items.")
        self.items = list(items)

    # Pass in items as an array.
    # Returns the eliminated item.
    def eliminate(self):
        if not self.items:
            raise ValueError("No more items to eliminate!")
        return self.items.pop(random.randint(0, len(self.items) - 1))

# Class for a Choose function
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

# Magic EightBall Class 
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

# Runs an alternative roulette simulation.
# Input is the starting number of valid positions.
# Returns result of spinning the roulette wheel & landing on a positon as a string.
def roulette(starting: int):
    if starting < 1 or starting > 6:
        raise ValueError("Starting number must be between 1 and 6.")
    
    rand_num = random.randint(1, 6)
    
    if rand_num <= starting:
        return "Unlucky, the end."
    else:
        return "Excellent, round passed."

# Flips a coin an arg number of times.
# Input is the number of times to flip the coin.
# Returns the flip results as a list.
def flipACoin(num: int) -> list[str]:
    if num <= 0:
        raise ValueError("Number of flips must be greater than zero.")
    return [random.choice(["Heads", "Tails"]) for _ in range(num)]

# Rolls a 6 sided dice an arg number of times.
# Input is the number of times to roll the dice.
# Returns the roll results as a list.
def rollADice(num: int) -> list[int]:
    if num <= 0:
        raise ValueError("Number of rolls must be greater than zero.")
    return [random.randint(1, 6) for _ in range(num)]

# Provides a random rock, paper, scissors outcome
# Takes no input
# Returns the rock, paper, scissors outcome as a string
def rockPaperScissors():
    outcomes = ['Rock', 'Paper', 'Scissors']
    return outcomes[random.randint(0, 2)]

# Generates a random hexcode color
# Input is number of colors generated
# Returns generated color hexcode(s) as string
def randomColorGenerator(num: int) -> list[str]:
    if num <= 0:
        raise ValueError("Must generate at least one color.")
    
    def colorGen():
        hex_color = ''
        for _ in range(6):
            hex_color += f"{random.randrange(0, 16):x}"
        return hex_color
    
    if num == 1:
        return colorGen()
    
    return [colorGen() for _ in range(num)]