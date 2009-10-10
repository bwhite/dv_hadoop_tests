#!/usr/bin/env python
"""Basic word count mapper.
Map: Produces "word 1" for each word in the given text.
Reduce: Collects the totals for each word and returns them as "word #"
Usage:

"""
import sys
import re
import operator
import itertools

def read_words():
    """Reads stdin, returns an iterator providing each word in the file (split by whitespace)."""
    for line in sys.stdin:
        for re_group in re.finditer('(\w+)', line):
            yield re_group.group(1)

def mapper(separator='\t'):
    for word in read_words():
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
