import sys
import math
tot=0
k=len(sys.argv)
print("Size=", k)
print(sys.argv[0])
min=math.inf
for i in range(1,k):
    if int(sys.argv[i])<min:
        min=int(sys.argv[i])

print("Minimum =",min)

