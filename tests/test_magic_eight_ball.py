import pytest
from devdice import MagicEightBall

def test_shake():
    ball = MagicEightBall()
    assert ball.shake() in ball.responses


def test_shake_no_responses():
    ball = MagicEightBall()
    ball.responses = ()
    with pytest.raises(ValueError):
        ball.shake()


def test_shake_response_type():
    ball = MagicEightBall()
    response = ball.shake()
    assert isinstance(response, str), "Magic 8-Ball response should be a string"
