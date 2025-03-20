from devdice import Chooser, Eliminator, MagicEightBall, roulette, flip_a_coin, roll_a_dice, rock_paper_scissors, random_color_generator
# Introduction and scope
print("Welcome to DevDice, the all in one Python Package for adding randomness to your projects.")
print("This package includes the following functions:\n\t1. flip_a_coin\n\t2. roll_a_dice\n\t3. MagicEightBall\n\t4. roulette\n\t5. Chooser\n\t6. Eliminator\n\t7. rock_paper_scissors\n\t8. random_color_generator")
print("This program will now demonstrate the complete functionality of DevDice.\n\n")

# Each function is demonstrated and includes the following structured information:
# Function - {Function call}
# Input - {Input specifications}
# Output - {Output specifications}
# Demo - {Example function demonstration with input/output}

# flip_a_coin() demo
print("1. Flipping a coin...")
print("\t Function - flip_a_coin()")
print("\t Input - Accepts any integer")
print("\t Output - A list of random selections as strings from ['Heads', 'Tails']")
print("\t Demo - flip_a_coin(5) results in", flip_a_coin(5), "\n")

# roll_a_dice() demo
print("2. Rolling a dice...")
print("\t Function - roll_a_dice()")
print("\t Input - Accepts any integer")
print("\t Output - A list of random selections as integers from [1, 2, 3, 4, 5, 6]")
print("\t Demo - roll_a_dice(5) results in", roll_a_dice(5), "\n")

# MagicEightBall.shake() demo
demo_magic_8_ball = MagicEightBall()
print("3. Asking the Magic 8 Ball...")
print("\t Function - MagicEightBall.shake()")
print("\t Input - Accepts no input")
print("\t Output - A randomly selected Magic 8 Ball response")
print("\t Demo - MagicEightBall.shake() results in", "'", demo_magic_8_ball.shake(), "'", "\n")

# roulette() demo
print("4. Playing roulette...")
print("\t Function - roulette()")
print("\t Input - Accepts any integer from 1 to 6 as a starting point")
print("\t Output - A string indicating the spin result")
print("\t Demo - roulette(2) results in", roulette(2))
print("\t \t - roulette(5) results in", roulette(5), "\n")

# Chooser.pick() demo
demo_chooser = Chooser(["Blue", "Red", "Green", "Violet"])
print("5. Chosing from a list...")
print("\t Function - Chooser.pick()")
print("\t Input - Accepts no input")
print("\t Output - A randomly selected Chooser option Object")
print("\t Demo - A Chooser Object has been created with option of ['Blue', 'Red', 'Green', 'Violet']")
print("\t \t  - Chooser.pick() results in", demo_chooser.pick(), "\n")

# Eliminator.eliminate() demo
demo_eliminator = Eliminator(["New York", "Boston", "Miami", "Atlanta"])
print("6. Eliminating from a list...")
print("\t Function - Eliminator.eliminate()")
print("\t Input - Accepts no input")
print("\t Output - The Object that has been removed from the Eliminator")
print("\t Demo - An Eliminator Object has been created with option of ['New York', 'Boston', 'Miami', 'Atlanta']")
print("\t \t  - Eliminator.eliminate() results in", demo_eliminator.eliminate(), "\n")

# rock_paper_scissors() demo
print("7. Playing Rock, Paper, Scissors...")
print("\t Function - rock_paper_scissors()")
print("\t Input - Accepts any integer")
print("\t Output - A list of random selections as strings from ['Rock', 'Paper', 'Scissors']")
print("\t Demo - rock_paper_scissors(3) results in", rock_paper_scissors(3), "\n")

# random_color_generator() demo
print("8. Generating a random color...")
print("\t Function - random_color_generator()")
print("\t Input - Accepts any integer")
print("\t Output - A list of random hex-code colors as strings")
print("\t Demo - random_color_generator(3) results in", random_color_generator(3), "\n")

print("Thank you for using DevDice!", end="")