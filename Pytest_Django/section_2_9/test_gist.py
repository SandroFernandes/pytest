import pytest


def test_our_first_test() -> None:
    assert 1 == 1


@pytest.mark.skip(reason="No need to run this test")
def test_skip_test() -> None:
    assert 1 == 2


@pytest.mark.skipif(0 > 1, reason="skipped because 0>1")
def test_should_be_skip_if() -> None:
    assert 1 == 1


@pytest.mark.skipif(3 > 1, reason="skipped because 3>1")
def test_should_be_skip_if_condition_false() -> None:
    assert 1 == 2


@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    assert 1 == 2


@pytest.mark.slow
def test_slow_test() -> None:
    assert 1 == 1
