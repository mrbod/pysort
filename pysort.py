#!/usr/bin/env python
import sys
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-k', '--key', type=int, default=0,  help='1 based sort key')
ap.add_argument('-s', '--skip', type=int, default=0, help='skip leading')
ap.add_argument('-c', '--convert', type=eval, default=None, help='convert key')
ap.add_argument('-r', '--reversed', action='store_true', help='reverse result')
args = ap.parse_args()

lines = sys.stdin.readlines()
data = [(i, l.strip().split()) for i, l in enumerate(lines)]
if args.skip > 0:
    data = data[args.skip:]
    sys.stdout.write(''.join(lines[:args.skip]))

def key(x):
    d = x[1][args.key - 1]
    if args.convert:
        return args.convert(d)
    return d

try:
    data.sort(key=key)
except Exception as e:
    sys.stderr.write('error: {}\n'.format(str(e)))
    sys.exit(1)

if args.reversed:
    data.reverse()

for d in data:
    #print d
    sys.stdout.write(lines[d[0]])

