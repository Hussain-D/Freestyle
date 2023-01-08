def p(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
    if count == 2:
        return True

def pl(num1):
    li = []
    for i in range(2,num1+1):
        if p(i):
            li.append(i)
    return li

nu = int(input())
# nu = (nu*(nu+1))//2
# print((nu))

print(pl(nu))