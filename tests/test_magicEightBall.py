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


def test_start_simulation(monkeypatch, capsys):

    ball = MagicEightBall()

    inputs = iter(["Will I pass?", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    ball.start_simulation()

    captured = capsys.readouterr()
    assert any(resp in captured.out for resp in ball.responses), "Expected a response in output"
    assert "Goodbye!" in captured.out, "Expected exit message in output"