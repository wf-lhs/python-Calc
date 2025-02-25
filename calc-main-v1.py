print("""
input at the mode section
1 = addition
2 = subtraction
3 = multiplication
4 = division
5 = long addition
""")
print("mode")
mode = int(input())
if mode == 1:
    print("num 1")
    i = float(input())
    print("num 2")
    ii = float(input())
    print(i,"+",ii,"=",i+ii)
if mode == 2:
    print("num 1")
    i = float(input())
    print("num 2")
    ii = float(input())
    print(i,"-",ii,"=",i-ii)
if mode == 1:
    print("num 1")
    i = float(input())
    print("num 2")
    ii = float(input())
    print(i,"x",ii,"=",i*ii)
if mode == 4:
    print("num 1")
    i = float(input())
    print("num 2")
    ii = float(input())
    print(i,"/",ii,"=",i/ii)
if mode == 5:
    numcount = int(input('numcount= '))
    ii = 0
    iii = 0
    while ii < numcount:
        i = int(input('num'))
        iii = iii+i
        ii = ii+1
        print("total=",iii)

