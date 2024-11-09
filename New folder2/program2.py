n=int(input("Enter the number of terms "))
num1,num2=0,1
if n<=0:
    print("Please enter a positive integer greater than zero")
elif n==1:
    print("Fibonacci sequence upto" ,n,": ")
    print(num1)
else:
    print('Fibonacci sequence:')
    print(num1,end=' ')
    print(num2,end=' ')
    i=2
    while i<n:
        num3 =num1+num2
        print(num3,end=' ')
        num1=num2
        num2=num3
        i=i+1
