# Matrix multiplication 

y= [[2,1], [4, 3]]
z= [[1,2], [3, 4]]
x= [[0,0], [0, 0]]

print(range(len(y)))
print(len(y[0]))

for i in range(len(y)):
    for j in range(len(y[0])):
        x[i][j]= y[i][j]* z[i][j]
        print(x[i][j])


# N= 12

# def powercheck(N):
#     b=[]
#     if N % 2 == 1:
#         return False

#     elif N % 2 ==0:
#         a= N/2
#         b.append(a)

#     for i in b:
#         v= i%2
#         if v!= 0:
#             return False
#         else:
#             h= i/2
#             b.append(h)

        
# def powercheck(N):
#     if N==0:
#         return (print(False))   
    
#     if N==1:
#         return (print(True))   

#     while N%2==0:
#         N=N/2

#     if N==1 or N==-1:
#         return (print(True))     
#     else:
#         return (print(False))   
        
# powercheck(0)

# array= [1,2]

# for i in range(30):
#     if array[i]< 4000000:
#         a= array[i] + array[i+1]
#         array.append(a)

# evenarray= []
# for i in array:
#     if i%2==0:
#         evenarray.append(i)

# total= sum(evenarray)

# print(total)
