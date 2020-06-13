#! /usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='Fizzbuzz python3 implementation.')
parser.add_argument('iterations', type=int, help='Run fizzbuzz to this number.')
args = parser.parse_args()

for num in range(1, args.iterations + 1):
  if num % 3 == 0 and num % 5 == 0 :
    print("fizz buzz")
  elif num % 3 == 0 :
    print("fizz")
  elif num % 5 == 0 :
    print("buzz")
  else:
    print(num)
