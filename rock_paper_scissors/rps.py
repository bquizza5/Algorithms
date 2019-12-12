#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  
  if n == 1:
    return [['rock'],['paper'],['scissors']]
  elif n == 0:
    return [[]]
  else:
    newArr = []
    for i in rock_paper_scissors(n-1):
      newArr.append(i + ['rock'])
      newArr.append(i + ['paper'])
      newArr.append(i + ['scissors'])
      
    return newArr


# print(rock_paper_scissors(0))




# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')