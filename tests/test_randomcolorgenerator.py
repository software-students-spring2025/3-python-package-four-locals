import pytest
from devdice import randomColorGenerator

def test_randomColorGenerator_valid():
    colors = randomColorGenerator(5)
    assert len(colors) == 5
    
    for color in colors:
        assert len(color) == 6
        assert all(hex_char in "0123456789abcdef" for hex_char in color)

def test_randomColorGenerator_valid_no_args():
    color = randomColorGenerator()
    assert len(color) == 6
    assert all(hex_char in "0123456789abcdef" for hex_char in color)

def test_randomColorGenerator_zero():
    with pytest.raises(ValueError):
        randomColorGenerator(0)
        
def test_randomColorGenerator_negative():   
    with pytest.raises(ValueError):
        randomColorGenerator(-3)
