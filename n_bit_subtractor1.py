def full_subtractor(a, b, c):
    diff = (a ^ b) ^ c
    borrow = ((~a & b) | ((~a | b) & c))
    return diff, borrow

def n_bit_subtractor(a, b):
    borrow = 0
    result = []
    for i in range(len(a)-1,-1,-1):
        d,borrow = full_subtractor(int(a[i]), int(b[i]), borrow)
        result.append(str(d))
    result.reverse()
    return ''.join(result)

a = '000101'.zfill(8) #4
b = '000100'.zfill(8) #-5
print(n_bit_subtractor(a,b))