#!/usr/bin/env python

import sys

def main():
  colsums = [] # colsums are empty
  for line in sys.stdin:
    valarray = [float(v) for v in line.split()]
    if len(colsums) < len(valarray):
      colsums.extend([0. for _ in xrange(len(valarray) - len(colsums))])
    for col,val in enumerate(valarray):
      colsums[col] += val
  for col,sum in enumerate(colsums):
    print col, sum

if __name__=='__main__':
  main()
