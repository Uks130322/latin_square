import pytest
import testlib

from latin_square import latin_square_three


###################
# Structure asserts
###################


def test_doc() -> None:
    assert testlib.is_function_docstring_exists(latin_square_three)


###################
# Tests
###################


def test_latin_square_three() -> None:
    lst = latin_square_three()
    assert len(lst) > 11, 'Wrong size'

    for i in range(12):
        letters = [char for char in lst if char != '\n']
        assert (set(letters[0:3]) == set(letters[3:6]) == set(letters[6:9]) == set(letters[0:9:3]) ==
                set(letters[1:9:3]) == set(letters[2:9:3]) == {'A', 'B', 'C'}), 'Coincidence is found'
