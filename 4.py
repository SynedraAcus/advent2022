#! /usr/bin/env python3

# This is solution to both 4_1 and 4_2. The difference is whether you use
# `overlaps()` or `contains()` in line 29
from argparse import ArgumentParser
import re


def get_numbers(line, query_regex):
    return [int(x) for x in re.search(query_regex, line).groups()]


def overlaps(numbers):
    # Not actually used
    return numbers[0] <= number_1s[3] and numbers[2] <= numbers[1]


def contains(numbers):
    return (numbers[2] - numbers[0]) * (numbers[1] - numbers[3]) >= 0


parser = ArgumentParser()
parser.add_argument('-i', type=str, help='Input file')
args = parser.parse_args()

query_regex = re.compile('([\d]+)\-([\d]+),([\d]+)\-([\d]+)')
count = 0
for line in open(args.i):
    if overlaps(get_numbers(line.rstrip(), query_regex)):
        count += 1
print(count)