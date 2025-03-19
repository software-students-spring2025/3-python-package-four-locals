import pytest
from devdice import rockPaperScissors

def test_rockPaperScissors_valid():
    outcome = rockPaperScissors()
    assert outcome in ['Rock', 'Paper', 'Scissors']
