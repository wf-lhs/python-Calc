print("""
input at the mode section
0 = quit
1 = addition
2 = subtraction
3 = multiplication
4 = division
5 = long addition
6 = power / exponent
""")
print("mode")
mode = int(input())
if mode == 0:
    print("quitting")
    quit()
if mode == 1:#addition
    print("num 1")
    i = float(input())
    print("num 2")
    ii = float(input())
    print(i,"+",ii,"=",i+ii)
if mode == 2:#subtraction
    print("num 1")
    i = float(input())
    print("num 2")
    ii = float(input())
    print(i,"-",ii,"=",i-ii)
if mode == 3:#multiplication
    print("num 1")
    i = float(input())
    print("num 2")
    ii = float(input())
    print(i,"x",ii,"=",i*ii)
if mode == 4:#devision
    print("num 1")
    i = float(input())
    print("num 2")
    ii = float(input())
    print(i,"/",ii,"=",i/ii)
if mode == 5:#addition
    numcount = int(input('numcount: '))
    ii = 0
    iii = 0
    while ii < numcount:
        i = int(input('num:'))
        iii = iii+i
        ii = ii+1
        print("total =",iii)
if mode == 6: #power,exponent
    i = int(input("number:"))
    ii = int(input("to the power of:"))
    iii = i**ii
    print(iii)
