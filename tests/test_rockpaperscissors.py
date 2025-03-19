import pytest
from devdice import rockPaperScissors

def test_rockPaperScissors_valid():
    outcomes = rockPaperScissors(5)
    assert len(outcomes) == 5
    for outcome in outcomes:
        assert outcome in ['Rock', 'Paper', 'Scissors']
    
def test_rockPaperScissors_no_args():
    outcome = rockPaperScissors()
    assert outcome in ['Rock', 'Paper', 'Scissors']

def test_rockPaperScissors_zero():
    with pytest.raises(ValueError):
        rockPaperScissors(0)
        
def test_rockPaperScissors_negative():   
    with pytest.raises(ValueError):
        rockPaperScissors(-3)
