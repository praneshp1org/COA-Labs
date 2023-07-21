def add(a, b):
    n=max(len(a), len(b))
    a=a.zfill(n)
    b=b.zfill(n)
    result = ""
    carry=0
    for i in range(len(a)-1, -1, -1):
        sum = (int(a[i])+int(b[i])+carry)%2
        carry = (int(a[i])+int(b[i])+carry)//2 #floor divison
        result=str(sum)+result101
    return result, carry

def multiply(a, b):
    n=max(len(a), len(b))
    a = a.zfill(n)
    b = b.zfill(n)
    temp_a=''.zfill(n)
    for i in range(n-1, -1, -1):
        if(b[i]=="1"):
            temp_a, cr = add(temp_a, a)
            temp_a = str(cr)+temp_a if cr==1 else temp_a
        a=a+"0"
    return temp_a

# a = "1111" #15
# b = "1011" #11
a=input("Enter the first number: ")
b=input("Enter the second number: ")
print("Multiplication is: ")
print(multiply(a, b))
