import pytest
from devdice import Chooser

def test_pick():
    
    options = ["apple", "banana", "orange"]
    chooser = Chooser(options)

    assert chooser.pick() in options

def test_empty_init():
    
    with pytest.raises(ValueError):
        Chooser([])
