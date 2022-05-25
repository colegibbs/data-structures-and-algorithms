from code_challenges.merge_sort import merge_sort

def test_merge_sort():
  arr = [4, 23, 42, 16, 15]
  merge_sort(arr)
  actual = arr
  expected = [4, 15, 16, 23, 42]
  assert actual == expected

def test_merge_sort_reverse_sorted():
  arr = [20, 18, 12, 8, 5, -2]
  merge_sort(arr)
  actual = arr
  expected = [-2, 5, 8, 12, 18, 20]
  assert actual == expected

def test_merge_sort_few_uniques():
  arr = [5, 12, 7, 5, 5, 7]
  merge_sort(arr)
  actual = arr
  expected = [5, 5, 5, 7, 7, 12]
  assert actual == expected

def test_merge_sort_almost_sorted():
  arr = [2, 3, 5, 7, 13, 11]
  merge_sort(arr)
  actual = arr
  expected = [2, 3, 5, 7, 11, 13]
  assert actual == expected
