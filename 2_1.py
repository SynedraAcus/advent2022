#! /usr/bin/env python3

from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-i', type=str, help='Input file')
args = parser.parse_args()

move_values = {'X': 1, 'Y': 2, 'Z': 3}
moves = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
vict_values = {-2: 6, -1: 0, 0: 3, 1: 6, 2: 0}
score = 0
for line in open(args.i):
    opp, you = (line.rstrip().split(' '))
    score += move_values[you]
    score += vict_values[moves[you] - moves[opp]]
print(score)
