### TODO import the file
from countingsort import countingsort
import time
import random
import sys

ALG_NAME = "Couting Sort"
DATA_COUNT = 1000 if len(sys.argv) < 2 else int(sys.argv[1])
SHOW_DATA = False if len(sys.argv) < 3 else bool(sys.argv[2])

def is_asc_sorted(A):
    for i in range(0,len(A)-1):
        if A[i] > A[i+1]:
            return False
    return True

def call_alg():
    global A
    B = A[:]
    #print "B:",B
    #print "Max:",max(A)
    countingsort(A,B,max(A))
    A = B

#----------------------------------------------------------------
    
print '##',ALG_NAME,'##'
print 'n =',DATA_COUNT
## BEST CASE
A = []
for i in range(0,DATA_COUNT):
    A.append(i)

print "Best case"
START = time.clock()
if SHOW_DATA: print "0",A

call_alg()

if SHOW_DATA: print "1",A
END = time.clock()
print "WRONG!!!" if not is_asc_sorted(A) else "Time:", (END-START)

## AVERAGE CASE
A = []
for i in range(0,DATA_COUNT):
    A.append(int(random.random()*DATA_COUNT))

print "Average case"
START = time.clock()
if SHOW_DATA: print "0",A

call_alg()

if SHOW_DATA: print "1",A
END = time.clock()
print "WRONG!!!" if not is_asc_sorted(A) else "Time:", (END-START)

# WORST CASE
A = []
for i in range(DATA_COUNT,0,-1):
    A.append(i)

print "Worst case"
START = time.clock()
if SHOW_DATA: print "0",A

call_alg()

if SHOW_DATA: print "1",A
END = time.clock()
print "WRONG!!!" if not is_asc_sorted(A) else "Time:", (END-START)
