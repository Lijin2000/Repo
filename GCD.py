a=int (input("Enter the first  number:"))
b= int (input("Enter the second number:"))
r=0
if a>b:
    while b!=0:
        r=a%b
        a=b
        b=r
        print("GCD is" ,a,b)
elif a==0:
    print("GCD of ",a, "",b,"is" ,b)
elif b==0:
    print("GCD of ",a, "",b,"is" ,a)
else:
    while a!=0:
        r=b%a
        b=a
        a=r
        print("GCD is" ,b,a)
    
    
    
        
    
