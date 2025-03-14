import pytest
from devdice import roulette

def test_roulette():
    # run it 50 times & it should go off
    results = [roulette() for _ in range(50)]
    assert True in results