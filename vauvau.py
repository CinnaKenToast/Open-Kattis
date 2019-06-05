(a,b,c,d) = [int(x) for x in input().split()]
(p,m,g) = [int(x) for x in input().split()]

d1t = a + b
d2t = c + d

a1 = [False] * d1t
a2 = [False] * d2t

for x in range(0,a):
    a1[x] = True
for x in range(0,c):
    a2[x] = True
    
pt1 = a1[(p-1)%d1t]
pt2 = a2[(p-1)%d2t]
mt1 = a1[(m-1)%d1t]
mt2 = a2[(m-1)%d2t]
gt1 = a1[(g-1)%d1t]
gt2 = a2[(g-1)%d2t]


if pt1 == True and pt2 == True:
    print ("both")
elif pt1 == False and pt2 == False:
    print ("none")
else:
    print ("one")

if mt1 == True and mt2 == True:
    print ("both")
elif mt1 == False and mt2 == False:
    print ("none")
else:
    print("one")

if gt1 == True and gt2 == True:
    print ("both")
elif gt1 == False and gt2 == False:
    print ("none")
else:
    print ("one")
