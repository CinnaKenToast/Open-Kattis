num = int(input())
cook = []
for i in range(0,num):
    cook.append([int(x) for x in input().split()])
boil = False


maxstart=cook[0][0]
minend=cook[0][1]
for (a,b) in cook:
    if(a>maxstart):
        maxstart = a
    if(b<minend):
        minend = b


for(a,b) in cook:
    if(b < maxstart):
        boil = True
    if(a > minend):
        boil = True

if(boil == True):
    print('edward is right')
else:
    print('gunilla has a point')

    
    