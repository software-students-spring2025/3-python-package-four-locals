import pytest
from devdice import Eliminator

def test_eliminator():
    e = Eliminator(["a", "b", "c"])
    assert e.eliminate() in ["a", "b", "c"]
    assert len(e.items) == 2

    e.eliminate()
    e.eliminate()

    with pytest.raises(ValueError):
        e.eliminate()
