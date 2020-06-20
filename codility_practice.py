# def getfactorial(n):
#     factorial = 1
#     for i in range(1, n+1):
#         factorial*=i

#     return factorial

# print(getfactorial(4))


# for i in range(1, 5):
#     for j in range(i):
#         print ('* ' * j)
#     print

# def solution(n):

#     a= bin(n).replace("0b", "")
#     b= a.strip('0')
#     c= b.split('1')

#     return max([len(i) for i in c])



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

# J= [1,2,3,4,6]
# def solution(N):
#     a= min(N)
#     b= max(N)

#     for i in range(a, b+1):
#         if i not in N:
#             return i 

# print(solution(J))

# stack= [0,1,2,3,4,5,6,7,8,9]
# size= 0

# def push(x):
#     stack.append(x)

#     print (stack)

# push(8)

# def pop(x):
#     global size
#     size-=1
#     stack[size]= x



def summ(x):
    '''
    Function to get the 

    '''
    a=[]
    for i in range(0, x):
        if i%3 ==0 or i%5==0:
            a.append(i)
    
    return sum(a)

print(summ(10))

