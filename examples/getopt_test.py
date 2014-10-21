import sys
import getopt

options, args = getopt.getopt(sys.argv[1:], 'a:b:c:')
for op, p in options:  
    if op == '-a':
        print 'option a', p
    
    elif op == '-b':
        print 'option b', p
    
    elif op == '-c':
        print 'option c', p
    
    else:
        print 'Unknown option', op

print args