#! /usr/bin/env python3

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-i', type=str, help='Input file')
args = parser.parse_args()

move_values = {'X': 1, 'Y': 2, 'Z': 3}
req_move = {'A': {'X': 3, 'Y': 1, 'Z': 2},
            'B': {'X': 1, 'Y': 2, 'Z': 3},
            'C': {'X': 2, 'Y': 3, 'Z': 1}}
moves = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
vict_values = {-2: 6, -1: 0, 0: 3, 1: 6, 2: 0}
score = 0
for line in open(args.i):
    opp, req_result = (line.rstrip().split(' '))
    score += req_move[opp][req_result] # By a funny coincidence, I get to reuse
    score += vict_values[req_move[opp][req_result] - moves[opp]]
print(score)
