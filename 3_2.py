#! /usr/bin/env python3

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-i', type=str, help='Input file')
args = parser.parse_args()


def item_value(item):
    r = ord(item)
    if r >= 96:
        #Lowercase letters
        return r - 96
    else:
        # Uppercase letters
        return r - 38


total = 0
group = []
for line in open(args.i):
    group.append(line.rstrip())
    if len(group) == 3:
        tmp = [set(x) for x in group]
        shared = tmp[0].intersection(tmp[1]).intersection(tmp[2]).pop()
        total += item_value(shared)
        group = []
print(total)
