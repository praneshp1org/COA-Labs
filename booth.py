# # A<-0, Q-1 <-0, 
# # M=multiplicand, Q<- multiplier
# # Q0Q-1 = 10 A-M
# # 01 A+M
# # shift
# def add(a, m):
#     carry=0
#     sum=''
#     for i in range (len(a)-1, -1, -1):
#         temp = int(a[i]+int(m[i]))+carry
#         if(temp>1):
#             sum = sum+str(temp%2)
#             carry=1
#         else:
#             sum+=str(temp)
#             carry=0
#     return sum[::-1] #reversing the sum

# def complement(m):
#     m=''
#     for i in range (len(m)):
#         m+=str(int(m[i])+1)%2
#     a='0'*(len(m)-1)
#     a=a+"1"
#     m=add(m, a)
#     return m

# def boothAlgorithm(m, q):
#     a = '0'*len(m)
#     count =len(q)

#     comp_m = complement(m)
#     q = q[:]+"0"
#     while(count):
#         q1 = q[-2:] #extracting last two
#         if(q1=="10"):
#             a=add(a, comp_m)
#             print("Subtracting m from a and right shift")
#             q = a[-1]+q[0:-1]
#             #assigns the last character of string A to the beginning of string Q. It effectively right-shifts Q by one position, and the least significant bit from A becomes the most significant bit of Q.
#             a = a[0]+a[0:-1]
#         elif (q1=="01"):
#             a = add(a,a)
#             print("Add A and M and Right shift ")
#             q = a[-1]+q[0:-1]
#             a = a[0]+a[0:-1]
#         elif(q1=="00" or q1=="11"):
#             print("Right shift only ")
#             q = a[-1]+q[0:-1]
#             a = a[0]+a[0:-1]
#         count-=1
#     q = q[:-1]
#     print("Final anser is ", "A= ", a, "Q = ", Q)

# boothAlgorithm("1001", "1101")

def add(A, M): 
    carry = 0
    Sum = '' 

    for i in range (len(A)-1, -1, -1): 
        temp = int(A[i]) + int(M[i]) + carry 
        if (temp>1): 
            Sum += str(temp % 2) 
            carry = 1
        else: 
            Sum += str(temp) 
            carry = 0
    return Sum[::-1]     
  
def compliment(m): 
    M = '' 
  
    for i in range (len(m)): 
  
        # Computing the compliment 
        M += str((int(m[i]) + 1) % 2) 
    A='0'*(len(M)-1)
    A=A+"1"
    M = add(M, A) 
    return M

def BoothsAlgo(M,Q):
    A = '0'*len(M)
    count = len(Q) 
    comp_M = compliment(M) 

  
    Q = Q[:]+"0"
    while(count):
        q = Q[-2:]
        if(q=="10"):
            A=add(A,comp_M)
            print("Subtract M from A and right shift ")
            Q = A[-1]+Q[0:-1]
            A = A[0]+A[0:-1]
        elif (q =="01"):
            A = add(A,M)
            print("Add A and M and Right shift ")
            Q = A[-1]+Q[0:-1]
            A = A[0]+A[0:-1]
        elif(q=="00" or q=="11"):
            print("Right shift only ")
            Q = A[-1]+Q[0:-1]
            A = A[0]+A[0:-1]
        count-=1
    Q = Q[:-1]
    print("Final answer is ","A = ",A, "Q = ",Q)

BoothsAlgo("1101","1011")

        
