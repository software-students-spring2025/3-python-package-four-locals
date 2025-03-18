import pytest
from devdice import flipACoin

def test_flipACoin_valid():
    result = flipACoin(5)
    assert len(result) == 5
    assert all(coin in ["Heads", "Tails"] for coin in result)

def test_flipACoin_zero():
    with pytest.raises(ValueError):
        flipACoin(0)

def test_flipACoin_negative():   
    with pytest.raises(ValueError):
        flipACoin(-3)
