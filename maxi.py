import sys
import math
tot=0
k=len(sys.argv)
print("Size=", k)
print(sys.argv[0])
max=-math.inf
for i in range(1,k):
    if int(sys.argv[i])> max:
        max=int(sys.argv[i])

print("Maximum =",max)

