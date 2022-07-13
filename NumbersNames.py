x=int(input("enter a number :"))

if x>0 and x<10:
    arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
    print("the nuber in words:", arr[x])
    
elif x>9 and x<100:
    print("the number",x, "have 2 digit")
    y=int(x/10)
    z=int(x%10)
    sum1=int(y+z)
    print("the sum of the digits is: ",sum1)

elif x>99 and x<1000:
    print("the number",x, "have 3 digit")
    a=int(x/100)
    b=x%100
    b=int(b/10)
    c=x%100
    c=int(c%10)
    mul1=int(a*b*c)
    print("the multipla of the digits is: ",mul1)
else:
    print("Number out of range")
