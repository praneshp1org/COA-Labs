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

def nonRestoringDivison(Q, M):
    A='0'*len(Q)
    count = len(M)
    comp_M=complement(M)
    flag='successful'
    print('Initial Values: A:', A,' Q:', Q, ' M:', M)
    while(count):

        print("\nstep:", len(M) - count + 1,
        end='')
        print(' Left Shift and ', end='')
        A = A[1:] + Q[0]
        if(flag=='successful'):
            A=add(A, comp_M)
            print('Subtract: ')
        else:
            A=add(A, M)
            print("Addition: ")

        print('A:', A, ' Q:',Q[1:] + '_', end='')

        if(A[0]=='1'):
            Q = Q[1:] + '0'
            print('  -Unsuccessful')

            flag = 'unsuccessful'
            print('A:', A, ' Q:', Q,
                  ' -Addition in next Step')

        else:
            Q = Q[1:] + '1'
            print('  Successful')

            flag = 'successful'
            print('A:', A, ' Q:', Q,
                  ' -Subtraction in next step')
        count -=1
    print('\nQuotient(Q):', Q,
          ' Remainder(A):', A)
nonRestoringDivison('1111', '0111')
