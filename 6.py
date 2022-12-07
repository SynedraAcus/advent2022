#! /usr/bin/env python3

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-i', type=str, help='Input file')
parser.add_argument('--subproblem', type=str, default=1,
                    help='Which problem for the day? Either 1 or 2')
args = parser.parse_args()

if args.subproblem == '1':
    breakoff = 5
else:
    breakoff = 15
in_line = open(args.i).readline().rstrip()
cache = ''
for index, char in enumerate(in_line):
    cache += char
    if len(cache) == breakoff:
        cache = cache[1:]
    if len(set(cache)) == breakoff - 1:
        print(index + 1)
        break