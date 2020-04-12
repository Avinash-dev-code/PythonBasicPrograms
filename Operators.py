#This programm contains show you all operators for understanding.
#Arithmetic Operator
#Already Defined variable value
a=23
b=54
print("Addition operator:", a+b) #Addition operator
print("Substraction operator:", a-b) #Substraction operator
print("Division operator:", a/b) #Division operator
print("Multiplication operator:", a*b) #Multiplication operator
print("Modules operator", a%b) #Modules operator    
print("Integer division operator ", a//b)#Integer division operator
print("Exponent operator:", a**b)#Exponent
print("\n")
print("Below enter a  two numbers numbers for understanding arithmetic operator")
#Take input value from user
c=int(input()) #if you do not cast or declar any data type like int,decimal and all then by default they accept as a string.
d=int(input()) 
print("This is your first number:", c)
print("This is your second number:", d)

print("Addition operator:", c+d) #Addition operator
print("Substraction operator:", c-d) #Substraction operator
print("Division operator:", c/d) #Division operator
print("Multiplication operator:", c*d) #Multiplication operator
print("Modules operator", c%d) #Modules operator    
print("Integer division operator ", c//d)#Integer division operator
print("Exponent operator:", c**d)#Exponent
print("\n")
#Boolean Values
print("Below you understand the concept of boolean values")
isCorrect=True
print(isCorrect)
print("\n")
#Comparison Operators
print("Below enter two numbers for understanding comparison operator")
n=int(input())
m=int(input())
print("This is your first number:", n)
print("This is your second number:", m)
print("Equal to operator:", n==m)# Equal to operator
print("Not equals to operator:", n!=m)# Not equals to operator  
print("n is less than m:", n<m)# n is less than m
print("n is greater than m:", n>m)# n is greater than m
print("n less than quals to m:", n<=m)# nless than quals to m
print("n greater than equals to m:", n>=m)#n greater than equals to m
print("\n")
#Assignment Operators :-Assignment operators are used to assign values to variables:
print("Below enter two numbers for getting output for understanding assignment operator")
i=int(input())
j=int(input())
print("This is your first number:", i)
print("This is your second number:", j)
i+=j
i-=j
i*=j
i/=j
i//=j

print(i) #but output value you will get last operator that i assigned.

