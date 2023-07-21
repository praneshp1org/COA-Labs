def add(A, M):
    carry = 0
    Sum = ''
    for i in range(len(A) - 1, -1, -1):
        temp = int(A[i]) + int(M[i]) + carry

        if (temp > 1):
            Sum += str(temp % 2)
            carry = 1
        else:
            Sum += str(temp)
            carry = 0
    return Sum[::-1]

def complement(m):
    M = ''
    for i in range(len(m)):
        M+=str((int(m[i])+1)%2)

    A='0'*(len(M)-1)
    A = A+"1"
    M=add(M, A)
    return M

def restoringDivison(Q, M):
    A='0'*len(Q)
    count = len(M)
    print('Initial Values: A:', A,' Q:', Q, ' M:', M)
    while(count):
        print("\nstep:", len(M) - count + 1, end='')
        print(' Left Shift and Subtract: ', end='')
        A = A[1:] + Q[0]
        comp_M=complement(M)
        
        A = add(A, comp_M)
        print(' A:', A)
        print('A:', A, ' Q:', Q[1:] + '_', end='')

        if(A[0]=='1'):
            Q=Q[1:]+'0'
            A=add(A, M)
            print('A:', A, ' Q:', Q, ' -Restoration')
        else:
            Q = Q[1:] + '1'


            print('A:', A, ' Q:',Q, ' -No Restoration')
        count -=1
    print('\nQuotient(Q):', Q,
          ' Remainder(A):', A)

restoringDivison('1111', '0111') #15/4


