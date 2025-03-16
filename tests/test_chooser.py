import pytest
from devdice import Chooser

def test_pick():
    
    options = ["apple", "banana", "orange"]
    chooser = Chooser(options)
    assert chooser.pick() in options

def test_add_option():
    
    chooser = Chooser(["apple", "banana"])
    chooser.add_option("orange")
    assert "orange" in chooser.get_options()

def test_remove_option():
    
    chooser = Chooser(["apple", "banana", "orange"])
    chooser.remove_option("banana")
    assert "banana" not in chooser.get_options()

def test_remove_invalid_option():
    
    chooser = Chooser(["apple", "banana"])
    with pytest.raises(ValueError):
        chooser.remove_option("orange")

def test_empty_init():
    
    with pytest.raises(ValueError):
        Chooser([])
