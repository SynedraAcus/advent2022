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
for line in open(args.i):
    l = line.rstrip()
    i = int(len(line) / 2)
    comp1 = set(line[:i])
    comp2 = set(line[i:])
    shared = comp1.intersection(comp2).pop() # Assume a single item
    total += item_value(shared)
print(total)
