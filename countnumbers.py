a=int(input())
b=int(input())
f=0
while True:
    a=a+1
    if a%2==0:
        d=0
    elif a>=b:
        break
    else:
        f+=1
print(f)
