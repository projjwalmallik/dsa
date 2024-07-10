def pattern1(N):
    for i in range(N):
        print("* "*N)

pattern1(6) 

def pattern2(N):
    for i in range(N):
        print("* "*(i+1))

pattern2(4)

def pattern3(N):
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(f"{j}", end=" ")
        print("", end='\n')


pattern3(5)

def pattern4(N):
    for i in range(N):
        print(f"{i} "*(i+1))

pattern4(4)

def pattern5(N):
    for i in range(N, 0,-1):
        print("* "*i)

pattern5(5)

def pattern6(N):
    j = N
    while(j>0):
        for i in range(1, j+1):
            print(f"{i} ", end=" ")
        print(" ", end="\n")
        j -= 1

pattern6(4)

def pattern7(N):
    for i in range(1, N+1):
        print(" "*(N-i)+"* "*i)

pattern7(5)

def pattern8(N):
    for i in range(N, 0, -1):
        print(" "*(N-i)+"* "*i)

pattern8(5)

def pattern9(N):
    for i in range(1, N+1):
        print(" "*(N-i)+"* "*i)
    for i in range(N, 0, -1):
        print(" "*(N-i)+"* "*i)
pattern9(6)

def pattern10(N):
    for i in range(1, N+1):
        print("* "*i)
    for i in range(N-1, 0, -1):
        print("* "*i)

pattern10(5)

def pattern11(N):
    k = 1
    for i in range(1, N+1):
        for j in range(1, i+1):
            if k==True:
                print("1 ", end=" ")
            if k==False:
                print("0 ", end=" ")
            k = not k
        print(" ", end="\n")
pattern11(4)

def pattern12(N):
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(f"{j}", end=" ") 
    
        print(" "*(((N-i)*2)*2), end="")
        for k in range(i, 0, -1):
            print(f"{k}", end=" ")
        print("", end="\n")
pattern12(4)

def pattern13(N):
    j = 1
    for i in range(1, N+1):
        for k in range(1, i+1):
            print(f"{j}", end=' ')
            j +=1
        print("", end="\n")

pattern13(5)

def pattern14(N):
    for i in range(1,N+1):
        for j in range(i):
            print(chr(65+j), end="")
        print("", end="\n")

pattern14(5)

def pattern15(N):
    for i in range(N, 0, -1):
        for j in range(i):
            print(chr(65+j), end="")
        print("", end="\n")

pattern15(5)

def pattern16(N):
    j = 0
    for i in range(1, N+1):
        print((chr(65+j)+ " ")*i)
        j+=1

pattern16(5)

def pattern17(N):
    for i in range(1, N+1):
        print(" "*(N-i), end="")
        k=0
        for j in range(1, i+1):
            print(chr(64+j), end="")
        for l in range(i, 0, -1):
            print(chr(64+l)*k, end="")
            k=1
        print("", end="\n")    

pattern17(5)

def pattern18(N):
    for i in range(1, N+1):
        k=0
        for j in range(0, i):
            print(chr(65+N-i+k), end="")
            k+=1
        print("", end="\n")

pattern18(5)

def pattern19(N):
    for i in range(1, N+1):
        print("*"*(N-i+1), end="")
        print(" "*(i-1)*2, end="")
        print("*"*(N-i+1), end="\n")
    for i in range(1, N+1):
        print("*"*(i), end="")
        print(" "*(N-i)*2, end="")
        print("*"*(i), end="\n")

pattern19(5)

def pattern20(N):
    for i in range(1, N):
        print("*"*(i), end="")
        print(" "*(N-i)*2, end="")
        print("*"*(i), end="\n")
    for i in range(1, N+1):
        print("*"*(N-i+1), end="")
        print(" "*(i-1)*2, end="")
        print("*"*(N-i+1), end="\n")
pattern20(5)

def pattern21(N):
    for i in range(1, N+1):
        if i == 1 or i == N:
            print("*"*N, end="\n")
        else:
            print("*", end="")
            print(" "*(N-2), end="")
            print("*", end="\n")
pattern21(6)

def pattern22(N):
    for i in range(0, 2*(N-1)+1):
        for j in range(0, 2*(N-1)+1):
            top = i
            bottom =j
            right = (2*N -2) - j
            left = (2*N - 2) - i 
            print(N- min(min(top, bottom), min(left, right)), end=" ")
        print("", end="\n")
pattern22(4)
