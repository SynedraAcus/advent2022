#! /usr/bin/env python3

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-i', type=str, help='Input file')
parser.add_argument('--subproblem', type=str, default=1,
                    help='Which problem for the day? Either 1 or 2')
args = parser.parse_args()


class Node:
    def __init__(self, node_id='Placeholder node', type='file',
                 size=None, children=[]):
        self.node_id = node_id
        self._size = size
        self.type = type
        self.children = children
        self.parent = None

    @property
    def size(self):
        if self._size:
            return self._size
        else:
            self._size = sum(x.size for x in self.children)
            return self._size

    def add_child(self, child):
        assert isinstance(child, Node)
        child.parent = self
        self.children.append(child)

root = Node(node_id='/', type=dir)
current = root
dircache = [root]
for line in open(args.i):
    if line[0] == '$':
        # This is a command
        l = line.rstrip().split(' ')
        if l[1] == 'cd':
            if l[2] == '/':
                current = root
            elif l[2] == '..':
                current = current.parent
            else:
                for child in current.children:
                    if child.node_id == l[2] and child.type == 'dir':
                        current = child
                        break
        elif l[1] == 'ls':
            continue # Nothing to do with the line containing ls
    else:
        # This is output of dir
        l = line.rstrip().split(' ')
        if l[0] == 'dir':
            dir = Node(node_id=l[1], type='dir', children=[])
            current.add_child(dir)
            dircache.append(dir) # Cache all directories to avoid actual tree traversal
        else:
            current.add_child(Node(node_id=l[1], type='file', size=int(l[0])))

if args.subproblem == '1':
    print(f'Total size {root.size}')  # Needed to trigger lazy calculation of sizes
    total = 0
    for dir in dircache:
        if dir.size <= 100000:
            total += dir.size
    print(total)
elif args.subproblem == '2':
    needed = root.size - 40000000
    best = root.size
    for dir in dircache:
        if dir.size >= needed and dir.size < best:
            print(f'{dir.node_id}\t{dir.size}\t{needed}')
            best = dir.size
    print(best)
