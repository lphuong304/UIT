#plot a graph
n=int(input())
sum=0
def uoc(sum,n):
    for i in range(1,n-1):
        if n % i == 0:
            sum=sum+i
    return sum
print (uoc(sum,n))

