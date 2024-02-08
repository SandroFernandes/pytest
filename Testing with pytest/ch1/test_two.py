import pytest


@pytest.mark.xfail
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)


def test_error():
    raise ValueError("This should fail")


def f(x):
    return x / 0


def test_fail_function():
    assert f(1) == 2
