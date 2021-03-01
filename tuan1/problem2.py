x=int(input())
def find_fibo(x):
    if x<=2:
        return 1
    a,b,c=0,1,1
    count=0
    result=1
    while count<=30:
        c=a+b
        if count==x:
            result=a
        a=b
        b=c
        count=count+1
    return result
if x>=1 and x<=30 :
    print(find_fibo(x))
else:
    print('So', x ,'khong nam trong khoang [1,30].')