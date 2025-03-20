import pytest
from devdice import Chooser

def test_pick():
    
    options = ["apple", "banana", "orange"]
    chooser = Chooser(options)

    assert chooser.pick() in options


def test_pick_one_option():

    chooser = Chooser(["onlyone"])
    assert chooser.pick() == "onlyone"


def test_add_option():

    chooser = Chooser(["apple", "banana"])
    chooser.add_option("cherry")

    assert "cherry" in chooser.options, "Cherry should be in options"


def test_remove_nonexistent_option():
    
    chooser = Chooser(["apple", "banana"])
    
    with pytest.raises(ValueError):
        chooser.remove_option("grape")


def test_empty_init():
    
    with pytest.raises(ValueError):
        Chooser([])
