t=int(input())
for i in range(0,t):
    rem=0
    count=0
    n=int(input())
    a=n;
    while(int(a)>0):
        digit=int(a)%10;
        if(int(digit)!=0 and n%int(digit)==0):
            count=count+1  
        a=a/10;
    print(count)
        
