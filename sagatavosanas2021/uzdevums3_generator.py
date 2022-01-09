# -*- coding: utf-8 -*-
import random

#N = 100
#theSeed = 1
#fileName = "uzd03test4.txt"

#N = 100
#theSeed = 0
#fileName = "uzd03test5.txt"

#N = 1000
#theSeed = 0
#fileName = "uzd03test7.txt"

#N = 100000
#theSeed = 0
#fileName = "uzd03test10.txt"



#N = 100
#theSeed = 1
#fileName = "uzd03test4.txt"

#N = 1000
#theSeed = 0
#fileName = "uzd03test6.txt"

#N = 10000
#theSeed = 0
#fileName = "uzd03test8.txt"

N = 100000
theSeed = 0
fileName = "uzd03test10.txt"


with open(fileName, 'w') as myfile:
    myfile.write('{}'.format(N))
    myfile.write('\n')
    random.seed(theSeed)
    theEnd = random.randint(N//2, N)
    for i in range(1, theEnd):
        myfile.write('{} {}'.format(i,i+1))
        myfile.write('\n')
    for i in range(theEnd+1, N+1):
        myfile.write('{} {}'.format(theEnd, i))
        myfile.write('\n')


## Fully random tree
# vertices = list(range(1, N+1))
# subsets = list(range(1, N+1))
# edges = []
# remainingEdges = N-1
# random.seed(theSeed)
# while remainingEdges > 0:
#     uu = random.randint(1, N)
#     vv = random.randint(1, N)
#     if subsets[uu-1] == subsets[vv-1]:
#         continue
#     val1 = subsets[uu-1]
#     val2 = subsets[vv-1]
#     for ii in range(0, len(subsets)):
#         if subsets[ii] == val2:
#             subsets[ii] = val1
#     edges.append((uu, vv))
#     remainingEdges -= 1
#     if remainingEdges % 10000 == 0:
#         print('remainingEdges = {}'.format(remainingEdges))
#
#
# with open(fileName, 'w') as myfile:
#     myfile.write('{}'.format(N))
#     myfile.write('\n')
#     for edge in edges:
#         myfile.write('{} {}'.format(edge[0], edge[1]))
#         myfile.write('\n')
