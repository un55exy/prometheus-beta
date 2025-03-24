import pytest
from src.find_first_last_occurrence import find_first_last_occurrence

def test_find_first_last_occurrence_normal_case():
    arr = [1, 2, 2, 2, 3, 4, 5, 5]
    assert find_first_last_occurrence(arr, 2) == (1, 3)
    assert find_first_last_occurrence(arr, 5) == (6, 7)

def test_find_first_last_occurrence_single_element():
    arr = [1, 1, 1, 1]
    assert find_first_last_occurrence(arr, 1) == (0, 3)

def test_find_first_last_occurrence_not_found():
    arr = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 6) == (-1, -1)
    assert find_first_last_occurrence(arr, 0) == (-1, -1)

def test_find_first_last_occurrence_empty_array():
    arr = []
    assert find_first_last_occurrence(arr, 1) == (-1, -1)

def test_find_first_last_occurrence_large_array():
    arr = [1] * 100 + [2] * 100 + [3] * 100
    assert find_first_last_occurrence(arr, 1) == (0, 99)
    assert find_first_last_occurrence(arr, 2) == (100, 199)

def test_find_first_last_occurrence_first_last_elements():
    arr = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 1) == (0, 0)
    assert find_first_last_occurrence(arr, 5) == (4, 4)

def test_find_first_last_occurrence_type_mix():
    arr = [1, 2, 2.0, 3.14, 4, 5]
    assert find_first_last_occurrence(arr, 2) == (1, 2)
    assert find_first_last_occurrence(arr, 2.0) == (1, 2)