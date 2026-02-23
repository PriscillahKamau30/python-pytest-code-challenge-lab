# Import pytest and the function to test
import pytest
from lib.palindrome import longest_palindromic_substring

# ----------------------------
# BASIC TEST CASES
# ----------------------------

def test_babad():
    # 'bab' or 'aba' are both valid
    assert longest_palindromic_substring("babad") in ["bab", "aba"]

def test_cbbd():
    # 'bb' is the longest palindrome
    assert longest_palindromic_substring("cbbd") == "bb"

# ----------------------------
# EDGE CASES
# ----------------------------

def test_single_character():
    # A single character is always a palindrome
    assert longest_palindromic_substring("a") == "a"

def test_two_different_characters():
    # Either character is valid
    assert longest_palindromic_substring("ac") in ["a", "c"]

def test_entire_string_is_palindrome():
    # The whole string is a palindrome
    assert longest_palindromic_substring("racecar") == "racecar"

def test_empty_string():
    # Empty string should return empty
    assert longest_palindromic_substring("") == ""

def test_long_string():
    # Checks longer string
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

# ----------------------------
# SPECIAL CASES
# ----------------------------

def test_numbers():
    # Palindrome numbers
    assert longest_palindromic_substring("12321") == "12321"

def test_mixed_letters():
    # Even-length palindrome
    assert longest_palindromic_substring("abccba") == "abccba"