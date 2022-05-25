from multiprocessing import cpu_count

class EmptyStringError(Exception):
  pass

def roman_numeral(roman):
  if roman == "":
    raise EmptyStringError("String can't be empty.")

  roman = convert(list(roman))

  current = 0
  next = 1
  while next < len(roman):
    if roman[current] < roman[next]:
      roman[current] = -roman[current]

    current += 1
    next += 1

  return sum(roman)

def convert(roman):
  roman_rule = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
  }

  return [roman_rule[char] for char in roman]
