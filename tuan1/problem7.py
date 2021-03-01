xxx, yy= map(int, input().split())
def loop(xxx,yy):
    i=0
    while i<=xxx:
        j=xxx-i
        if i*4+j*2==yy:
                print (j,i)
                break
        i=i+1
loop(xxx,yy)