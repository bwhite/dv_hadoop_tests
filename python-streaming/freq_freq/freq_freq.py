#!/usr/bin/env python
"""Frequency of Frequency calculator
Map: Produces (freq, 1)" for each histogram line given
Reduce: Collects the frequencies and returns (freq, freq_freq)
Usage:

"""
import sys
import operator
import itertools

def read_freq():
    for line in sys.stdin:
        yield line.rstrip().split()[1]

def mapper(separator='\t'):
    for word in read_freq():
        print('%s%s1'%(word, separator))

def read_word_hists(separator='\t'):
    for line in sys.stdin:
        yield line.rstrip().split(separator, 1)

def reducer(separator='\t'):
    data = itertools.groupby(read_word_hists(), operator.itemgetter(0))
    for word, group in data:
        word_total = sum(int(count) for word, count in group)
        print('%s%s%d'%(word, separator, word_total))
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__)
        exit(1)
    method = sys.argv[1]
    if method == 'map':
        mapper()
    elif method == 'reduce':
        reducer()
    else:
        print(__doc__)
