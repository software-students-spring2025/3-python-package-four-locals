import pytest
from devdice import rockPaperScissors

def test_rock_paper_scissors_valid():
    '''
    Runs 5 r-p-s simulations and tests to make sure the outcomes are valid.
    '''
    outcomes = rockPaperScissors(5)
    assert len(outcomes) == 5
    for outcome in outcomes:
        assert outcome in ['Rock', 'Paper', 'Scissors']

def test_rock_paper_scissors_no_args():
    '''
    Runs r-p-s with no arguments.
    '''
    outcome = rockPaperScissors()
    assert outcome in ['Rock', 'Paper', 'Scissors']

def test_rock_paper_scissors_zero():
    '''
    Runs r-p-s with argument 0.
    '''
    with pytest.raises(ValueError):
        rockPaperScissors(0)

def test_rock_paper_scissors_negative():
    '''
    Runs r-p-s with a negative argument.
    '''
    with pytest.raises(ValueError):
        rockPaperScissors(-3)
