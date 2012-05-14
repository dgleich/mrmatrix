#!/usr/bin/env python

import sys

def main():
  for line in sys.stdin:
    valarray = [float(v) for v in line.split()]
    print sum(valarray)

if __name__=='__main__':
  main()
