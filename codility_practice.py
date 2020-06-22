# List of Algorithms/Functions from Codility practices

def getfactorial(n):
    '''
    Get the factorial of a given number
    '''
    factorial = 1
    for i in range(1, n+1):
        factorial*=i

    return factorial

# Algorithm to determine maximum number of consecutive 1s in a Binary number

def solution(n):

    a= bin(n).replace("0b", "")
    b= a.strip('0')
    c= b.split('1')

    return max([len(i) for i in c])



# def max_gap(N):
#     xs = bin(N)[2:].strip('0').split('1')
#     return max([len(x) for x in xs])

# print(solution(300))

# def negativetemp(temperatures):

#     days= 0
#     for temp in temperatures:
#         if temp<0:
#             days+=1

#     return days 


# array= [1,2,3,4,5,6,7,8]

# def reverseArray(A):

#     a= len(A)
#     for i in range(a//2):
#         k= a-i- 1
#         A[i], A[k]= A[k], A[i]
    
#     return A

# print(reverseArray(array))

# def solution(A, k):
#     A= 

# print(5%4)

# def count(n):
#     B=0
#     for i in range (1, n+1):
#         B+=i
#     return B

# print(count(2))

# Pushing and poping Values from a stack

J= [1,2,3,4,6]
def solution(N):
    a= min(N)
    b= max(N)

    for i in range(a, b+1):
        if i not in N:
            return i 

print(solution(J))

# Pushing and poping Values from a stack

stack= [0,1,2,3,4,5,6,7,8,9]
size= 0

def push(x):
    '''
    push a value to the stack
    '''
    stack.append(x)

push(8)

def pop(x):
    '''
    Removing a value from the stack
    '''
    global size
    size-=1
    stack[size]= x


# Function to get the sum of numbers divisible by 3 and 5 for a given number  

def summ(x):
    '''
    Algorithm to get the sum of numbers divisible by 3 and 5 
    between 1 and a given number  
    '''
    a=[]
    for i in range(0, x):
        if i%3 ==0 or i%5==0:
            a.append(i)
    
    return sum(a)


