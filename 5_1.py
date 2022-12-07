#! /usr/bin/env python3

from argparse import ArgumentParser
import re

parser = ArgumentParser()
parser.add_argument('-i', type=str, help='Input file')
parser.add_argument('--subproblem', type=str, default=1,
                    help='Which problem for the day? Either 1 or 2')
args = parser.parse_args()


def get_row(line):
    """
    Convert input line into a series of letters corresponding to crate IDs
    :param line:
    :return:
    """
    r = ''
    # Split into groups of 4
    for index in range(int(len(line) / 4) + 1):
        r += line[index * 4 + 1]
    return r


def get_command(line):
    """
    Convert input line into a series of numbers corresponding to a command
    :param line:
    :return:
    """
    return [int(x) for x in re.search('move ([\d]+) from ([\d]+) to ([\d+])',
                                      line).groups()]


parse_fun = get_row
outlist = []
for line in open(args.i):
    if line == '\n':
        # Empty line denotes end of stacks and beginning of commands
        tmp_stacks = outlist
        outlist = []
        parse_fun = get_command
        continue
    if line[1] == '1':
        # Skip the line with stack numbers
        continue
    else:
        outlist.append(parse_fun(line.rstrip()))

commands = outlist
stacks = [[] for _ in range(len(tmp_stacks[-1]))]
for stack in tmp_stacks:
    for index, value in enumerate(stack):
        if value != ' ':
            stacks[index].append(value)

if args.subproblem == '1':
    # Moving crates one by one
    for command in commands:
        for _ in range(command[0]):
            stacks[command[2] - 1].insert(0, stacks[command[1] - 1].pop(0))
elif args.subproblem == '2':
    # Moving crates in groups
    for command in commands:
        subset = stacks[command[1] - 1][0:command[0]]
        stacks[command[2] - 1] = subset + stacks[command[2] - 1]
        del(stacks[command[1] - 1][0: command[0]])
print(''.join(stack[0] for stack in stacks))