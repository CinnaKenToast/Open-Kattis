num = []
num = input().split()
num = [int(x) for x in num]
num.sort()
if(num[1]-num[0] == num[2]-num[1]):
    diff = num[1] - num[0]
else:
    diff = num [2] - num [1]
if(num[1] - num[0] != diff):
    print (num[0] + diff)
elif(num[2] - num[1] != diff):
    print (num[1] + diff)
else:
    print (num[2] + diff)
