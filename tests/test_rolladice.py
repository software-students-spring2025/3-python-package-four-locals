import pytest
from devdice import rollADice

def test_rollADice_valid():
    result = rollADice(5)
    assert len(result) == 5
    assert all(1 <= roll <= 6 for roll in result)

def test_rollADice_zero():
    with pytest.raises(ValueError):
        rollADice(0)

def test_rollADice_negative():
    with pytest.raises(ValueError):
        rollADice(-2)
