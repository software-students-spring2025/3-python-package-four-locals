[![CI / CD](https://github.com/software-students-spring2025/3-python-package-four-locals/actions/workflows/build.yaml/badge.svg)](https://github.com/software-students-spring2025/3-python-package-four-locals/actions/workflows/build.yaml)

# Software Engineering, Spring 2025, Project 3.

## Description

This Python package allows developers to use fun randomizing functions to flip a coin, roll a dice, generate random colors, choose an option from a list, and much more!

## PyPI Website Link

You can find the link to our package on the PyPI website [here](https://test.pypi.org/project/devdice/).

## Installation

Install the `devdice` module with pip:
```
pip install devdice
```

## Importing `devdice` Functions

You can use any function in your own projects by it importing `devdice` then calling it directly:
```
from devdice import{
    flipACoin,
    rollADice,
    MagicEightBall,
    roulette,
    Chooser,
    Eliminator,
    rockPaperScissors,
    randomColorGenerator
}

# Flip a coin 5 times
print(flipACoin(5)) # Possible Output: ['Heads', 'Heads', 'Heads', 'Heads', 'Tails']

# Generate two rock, paper, scissors outcomes
print(rockPaperScissors(2)) # Possible Output: ['Scissors', 'Rock']
```

## Usage Examples

### `Eliminator` Class
```
elim = Eliminator(['Option A', 'Option B', 'Option C'])
print(elim.eliminate()) # Removes and returns a random option
```

### `Chooser` Class
```
chooser = Chooser(['Option A', 'Option B', 'Option C'])
print(chooser.pick()) # Returns a randomly selected option
```

### `MagicEightBall` Class
```
magic_eight_ball = MagicEightBall()
print(magic_eight_ball.shake()) # Returns a randomly selected Magic Eight Ball response
```

### `roulette(starting: int)`
```
print(roulette(2)) # Spins wheel with 2 of 6 winning positions 
```

### `flipACoin(num: int)`
```
print(flipACoin(5)) # Flips 5 coins
```

### `rollADice(num: int)`
```
print(rollADice(5)) # Rolls 5 dice
```

### `rockPaperScissors(num: int = 1)`
```
print(rockPaperScissors()) # Generates a rock, paper, scissors outcome
print(rockPaperScissors(2)) # Generates list of 2 rock, paper, scissors outcomes
```

### `randomColorGenerator(num: int = 1)`
```
print(randomColorGenerator()) # Generates a hex-codes color string
print(randomColorGenerator(2)) # Generates list of 2 hex-codes color strings
```

### Demonstrative Python Script

The repository contains a script called `demo.py` which you can find [here](./demo.py). This script demonstrates all available functions in the `devdice` package, including details on their expected inputs and outputs.

## Contributing to DevDice's development

- The code is licensed under the [GNU General Public License](./LICENSE)
- Please use GitHub issues to submit bugs and report issues
- Feel free to contribute to the code

## Environment Setup for Contributors

### Instructions for any developer ever

1. In your python project's directory, if you have not done so already, create a virtual environment.

2. Enter that virtual enviroment.

3. run the command '' in your terminal to install the package.

4. In the python file you would like to use the package, add `import devdice` to the top.

5. 

### Instructions for setting up any environment vartiables and importing any starter data

There are no environemnt variables or starter data necessary for the system to operate correctly when run.

### Instructions for any "secret" configuration files

There are no "secret" configuration files such as `.env` or anything of that nature.

## Contributors

*Ordered alphabetically by last-name:*

1. [Edwin Chen](https://github.com/Eracks1012)
2. [Benjamin DeWeese](https://github.com/bdeweesevans)
3. [John Ma](https://github.com/j4ma)
4. [Forrest Williams](https://github.com/Zeklin)