num = int(input())
x = []
s1 = 0
s2 = 0
flag = False

for i in range (num):
    line = input()
    for num in line:
        s1 = s1 + int(num)

    for j in range(int(line), -1, -1):
        s2 = sum(int(digit) for digit in str(j))
        if s2 == (s1 - 1):
            print(j) 
            flag = True
        if flag == True:
            flag = False
            break
    
    s1 = 0

    
