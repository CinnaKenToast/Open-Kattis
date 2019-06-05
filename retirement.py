(b,br,bsv,a,asv) = [int(x) for x in input().split()]

amin = (br-b)*bsv
dollar = 0
while dollar <= amin:
    dollar = dollar + asv
    a = a + 1
print(a)