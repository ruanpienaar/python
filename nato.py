"""
Conversion functions for the NATO Phonetic Alphabet.
"""

import re

# To save a lot of typing the code words are presented here
# as a dict, but feel free to change this if you'd like.
ALPHANUM_TO_NATO = {
    "A": "ALFA",
    "B": "BRAVO",
    "C": "CHARLIE",
    "D": "DELTA",
    "E": "ECHO",
    "F": "FOXTROT",
    "G": "GOLF",
    "H": "HOTEL",
    "I": "INDIA",
    "J": "JULIETT",
    "K": "KILO",
    "L": "LIMA",
    "M": "MIKE",
    "N": "NOVEMBER",
    "O": "OSCAR",
    "P": "PAPA",
    "Q": "QUEBEC",
    "R": "ROMEO",
    "S": "SIERRA",
    "T": "TANGO",
    "U": "UNIFORM",
    "V": "VICTOR",
    "W": "WHISKEY",
    "X": "XRAY",
    "Y": "YANKEE",
    "Z": "ZULU",
    "0": "ZERO",
    "1": "ONE",
    "2": "TWO",
    "3": "TREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINER",
}


"""
Convert a message to a NATO code word transmission.
"""
def transmit(message: str) -> str:
  if message == "":
    return ""
  p = re.compile('[A-Z0-9]+')
  phonetic_string = ""
  charUpper = ""
  for char in message:
    charUpper = char.upper()
    if p.match(charUpper):
      print(ALPHANUM_TO_NATO[charUpper]) 
      if phonetic_string == "":
        phonetic_string = ALPHANUM_TO_NATO[charUpper]
      else :
        phonetic_string = phonetic_string + " " + ALPHANUM_TO_NATO[charUpper]
  print(phonetic_string)
  return phonetic_string

"""
Convert a NATO code word transmission to a message.
"""
def receive(transmission: str) -> str:
  if transmission == "":
    return ""
  # replace ALPHANUM_TO_NATO keys with ALPHANUM_TO_NATO values
  # to create NATO_TO_ALPHANUM dict, not having to maintain 2 dicts.
  nato_to_alphanum = {}
  for k in ALPHANUM_TO_NATO:
    nato_to_alphanum[ALPHANUM_TO_NATO[k]] = k
  plain_string = ""
  for word in transmission.split():
    plain_string = plain_string + nato_to_alphanum[word]
  print(plain_string)
  return plain_string
  
  
if __name__ == "__main__":
    # execute only if run as a script
    receive("HOTEL ECHO LIMA LIMA OSCAR WHISKEY OSCAR ROMEO LIMA DELTA")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  