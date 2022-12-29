import pytest

from math_series.series import fibonacci, lucas, sum_series


def test_fibonacci():
    assert fibonacci


def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fibonacci_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_fibonacci_6():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected


def test_fibonacci_7():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_fibonacci_8():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected


def test_fibonacci_9():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected


def test_fibonacci_10():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


def test_lucas():
    assert lucas


def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_4():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_lucas_5():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas_6():
    actual = lucas(6)
    expected = 18
    assert actual == expected


def test_lucas_7():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_lucas_8():
    actual = lucas(8)
    expected = 47
    assert actual == expected


def test_lucas_9():
    actual = lucas(9)
    expected = 76
    assert actual == expected


def test_lucas_10():
    actual = lucas(10)
    expected = 123
    assert actual == expected


def test_sum_series_0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


