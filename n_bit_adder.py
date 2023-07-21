def full_adder(a, b, c):
    sum = (a ^ b) ^ c
    carry = ((a & b) | (b & c) | (c & a))
    return sum, carry

def n_bit_adder(a, b):
    carry = 0
    result = []
    for i in range(len(a)-1,-1,-1):
        s,c = full_adder(int(a[i]), int(b[i]), carry)
        result.append(str(s))
        carry = c
    if carry:
        result.append(str(carry))
    result.reverse()
    return ''.join(result)

a = '0101'.zfill(8)#4
b = '0100'.zfill(8)#-5
print(n_bit_adder(a,b))
