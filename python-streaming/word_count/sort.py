#!/usr/bin/env python
import sys

def main(separator='\t'):
    lines = [line.rstrip().split() for line in sys.stdin]
    lines.sort(lambda x, y: cmp(x[0], y[0]))
    for word, count in lines:
        print('%s%s%s'%(word, separator, count))

if __name__ == '__main__':
    main()
    
