from random import*

Athletes = ["a","b","c","d","e","f"]
Results = [10,11,12,41,98,42]
remove = []

def AR(A,R):
    AR = input("add-Add Athletes and thier Results\nsort-sort both list\nrank-checks Athletes theirs Results highest to lowest\nlist-is same as sort but but nicer\nwhat-What sport was played\nmm-to check who has highest score or who has the lowest\n")
    if AR == "add":
        A, R = add(Athletes,Results)
    elif AR == "sort":
        A, R = sort(Athletes,Results)
    elif AR == "rank":
        A, R == rank(Athletes,Results)
    elif AR == "list":
        A, R == list(Athletes,Results)
    elif AR == "mm":
        A, R == MM(Athletes,Results)
    elif AR == "dis":
        A, R == dis(Athletes,Results)
    elif AR == "what":
        print("The sport used was the javelin throw")
    else:
        print("error")

def add(Athletes,Results):
    N = input("Put a name\n")
    Athletes.append(N)
    P = input("input range or random\n")
    if P == "range":
        P2 = int(input("put a range\n"))
        while P2 >= 100:
            print("LAIR")
            P2 = int(input("put a range\n"))
        Results.append(P2)
    else:
        P2 = randint(0,100)
        print(P2)
        Results.append(P2)
    return(Athletes,Results)

def sort(Athletes,Results):
    print(Athletes)
    print(Results)
    return(Athletes,Results)

def rank(Athletes,Results):
    top,inimes = sort2(Athletes,Results)
    Results.reverse()
    Athletes.reverse()
    n = len(Results)
    nq = 1
    for i in range(0,n,1):
        print(nq)
        print(f"Name:{Athletes[i]}\nRange:{Results[i]}M")
        nq+=1
    return(Athletes,Results)

def sort2(Athletes,Results):
    abi_p = 0
    abi_i = ""
    n = len(Results)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if Results[i]>Results[j]:
                abi_p = Results[i]
                Results[i] = Results[j]
                Results[j] = abi_p
                abi_i = Athletes[i]
                Athletes[i] = Athletes[j]
                Athletes[j] = abi_i
    return(Athletes,Results)

def list(Athletes,Results):
    N1 = len(Results)
    print("who went first to last\n")
    for N in range(0,N1):
        print(N+1)
        print(f"Name:{Athletes[N]}\nRange:{Results[N]}\n")
    return(Athletes,Results)

def MM(Athletes,Results):
    k = input("do want max or min result\n")
    if k == "max":
        print(f"Name:{Athletes[Results.index(max(Results))]}\nRange:{max(Results)}M")
    else:
        print(f"Name:{Athletes[Results.index(min(Results))]}\nRange:{min(Results)}M")
    return(Athletes,Results)

def dis(Athletes,Results):
    return(Athletes,Results)


while True:
    AR(Athletes,Results)