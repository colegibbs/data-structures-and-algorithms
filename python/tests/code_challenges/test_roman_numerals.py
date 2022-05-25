from code_challenges.roman_numerals import convert, roman_numeral, EmptyStringError
import pytest

def test_convert():
  roman = ["M", "C", "M"]
  actual = convert(roman)
  expected = [1000, 100, 1000]
  assert actual == expected

def test_roman_numeral():
  actual = roman_numeral("MCM")
  expected = 1900
  assert actual == expected

def test_roman_numeral_larger():
  actual = roman_numeral("MCMLXXXIV")
  expected = 1984
  assert actual == expected

def test_roman_numeral_standard():
  actual = roman_numeral("MMXXI")
  expected = 2021
  assert actual == expected

def test_roman_numeral_empty_string():
  with pytest.raises(EmptyStringError):
    actual = roman_numeral("")
