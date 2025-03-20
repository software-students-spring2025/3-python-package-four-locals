import pytest
from devdice import MagicEightBall

def test_shake():
    ball = MagicEightBall()

    assert ball.shake() in ball.responses
