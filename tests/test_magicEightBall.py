import pytest
from devdice import MagicEightBall

def test_shake():

    ball = MagicEightBall()

    assert ball.shake() in ball.get_responses()


def test_add_response():

    ball = MagicEightBall()

    ball.add_response("Test")
    assert "Test" in ball.get_responses()


def test_remove_response():

    ball = MagicEightBall()

    response = ball.get_responses()[0]
    ball.remove_response(response)
    assert response not in ball.get_responses()


def test_remove_invalid_response():

    ball = MagicEightBall()

    with pytest.raises(ValueError):
        ball.remove_response("Nonexistent response")