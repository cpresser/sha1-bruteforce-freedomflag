#!/usr/bin/python3

import hashlib
import itertools
import sys

_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
_CHARS = '0123456789abcdefghijklmnopqrstuvwxyz'

cool_numbers = ['2017', '1337']

def rgb(triplet):
  return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]

def get_sha_colors(teststr):
  digest = hashlib.sha1(teststr.encode('utf8')).hexdigest()
  c = [(0,0,0)]*6
  for i in range (0,6):
    c[i] = rgb(digest[(i*6):(i*6+6)])
  return (c, digest[36:40])

def test_function(split_digest):
  (colors, remainder) = split_digest
  #if remainder in cool_numbers:
  #  print ("rem", remainder)
  #  return True
  a = 120
  for (r,g,b) in colors:
    if r < b:
      return False
    if r < g:
      return False
    if g + b > a:
      return False
  
  return True
  print (colors, remainder)

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

s = "cpresser "
it = 0
found = test_function(get_sha_colors(s))
for attempt in bruteforce(_CHARS, 10):
  it += 1
  if it % 1000 == 0:
    print ("iteration %d: %s" % (it, s + attempt))

  if test_function(get_sha_colors(s + attempt)):
    break

result = s + attempt

print ("found a match after %d iterations" % it)
print ("source %s, sha1:%s" % (result, hashlib.sha1(result.encode('utf8')).hexdigest()))
