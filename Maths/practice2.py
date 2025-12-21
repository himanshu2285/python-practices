# # common code snippits for python 

# # Reversing a string
# str = "Himanshu"
# print(str[::-1])   # traversing the string in reverse order

# # checking palindrome
# def is_palindrome(n):
#     return n == n[::-1]
# print(is_palindrome("123"))

# # counting frequency of elements in a list
# from collections import Counter
# lst = ['1','2','2','2','1']
# print(Counter(lst))

# # swapping two numbers
# a=10
# b=20
# a,b=b,a
# print(a,b)


# # Fibonacci series
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
# fib(10)


# # Factorial of a number
# def fact(n):
#     return 1 if n==0 or n==1 else n * fact(n-1)
# print(fact(5))


# for letter in "HImanshu":
#     pass
# print("letter", end=' ')

num = lambda x: x*x*x
print(num(5))