import pytest
from assertpy import assert_that


def test_simple_one():
    """Assert 2 is not None using standard assertion"""
    assert 2 is not None


def test_simple_two_fail():
    """2 < 1 failing test in pytest"""
    assert_that(2).is_less_than(1)


def test_simple_name(my_name):
    """Check name"""
    assert_that(my_name).is_equal_to('Adrian')


def test_simple_integers(random_positive_number):
    """Check random integer greater than 0"""
    assert_that(random_positive_number).is_greater_than(0)


def test_simple_integers_two(random_positive_number):
    """Check random integer between 0 and 100"""
    assert_that(random_positive_number).is_between(0, 100)


@pytest.mark.parametrize('test_input,expected', [('james', 'JAMES'), ('Anna', 'ANNa')])
def test_capitalize(test_input, expected):
    """Check if strings are correctly capitalized"""
    assert test_input.upper() == expected
