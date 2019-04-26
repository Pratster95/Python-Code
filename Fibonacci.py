def fibonacci(n):
    a=0
    b=1
    print ("The fibonacci series is:")
    print (a, end=" ")
    print (b, end=" ")
    for i in range(n-2):
       c=a+b
       a=b
       b=c
       print (c, end=" ")
    
      
       
fibonacci(10)

 
    
    