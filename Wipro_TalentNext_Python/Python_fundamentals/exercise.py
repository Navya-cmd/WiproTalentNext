#Q1. Write a program to check if a given number is Positive, Negative or Zero.

num = float(input("Enter NUmber"))
if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")    

#Q2. Write a program to check if a given number is odd or even.
num = int(input("Enter a number"))
if  num%2 == 0:
  print(number is even)
else:
    print("number is odd")  
   
# Q3.Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
a = int(input("Enter first non-negative number: "))
b = int(input("Enter second non-negative number: "))
print(a % 10 == b % 10)

#Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1, 11):
    print(i, end='\t')

# #Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

#Q6. Write a program to check if a given number is prime or not
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")       

 #Q7. Write a program to print prime numbers between 10 and 99.   
for num in range(10, 100):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

#Q8. Write a program to print the sum of all the digits of a given number.
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("Sum of digits:", sum)

#Q9.Write a program to reverse a given number and print.
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed number:", rev)

#Q10. Write a program to find if the given number is palindrom or not.
num = int(input("Enter a number: "))
original = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if original == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")