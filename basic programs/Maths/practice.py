



# def printname(name):   #keyword argument
#     print(name)
# printname("Himanshu")  # Call the function with a name

# def evenodd(num,random=29):
#     print(random)  # default argument
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    


#pass keyword
# def fun():
#     pass  
# fun()


# for i in range(1, 10, 2):
#     print(i)

# for loop with string
# name = "Himanshu"
# for i in name:
#     print(i)  # Print each character in the name with a space
# print(name[0])


#ternary operator
# num =45
# s = "Adult" if num >= 18 else "Minor"
# print(s)  # Output: Adult

# a = 5
# b = 2
# print(a // b)



# # conditional statements and loops
# # num = int(input("Enter number : "))
# # if num % 2 == 0:
# #     print("Even")
# # elif num == 0:
# #     print("Zero")
# # else:
# #     print("Odd")

# #LIST
# # list = ["himanshu0","mohit","sachin","priyanshu","himanshu1"]
# # for i in list:
# #     if i.startswith("himanshu"):
# #         print(i, len(i),end=" ")

# #DICTIONARY
# # users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# # for user, status in users.copy().items():
# #     print(user, status)

# # coll2 = {0:"Himanshu", 1:"Mohit", 2:"Sachin", 3:"Priyanshu", 4:"Himanshu1"}
# # print(type(coll2))


# # while loop
# # num = 0
# # while num < 10:
# #     print(num)
# #     num += 1

# # for loop with range
# # for i in range(3, 10):
# #    print(i)

# # for i in range(1, 10, 2):
# #     if i == 5:
# #         continue
# #     print(i)    
# # range(first, last, step)

# # a = ['Mary', 'had', 'a', 'little', 'lamb']
# # for i in range(len(a)):
# #     print(i, a[i])

# #BREAK STATEMENT
# # for n in range(2, 10):
# #     for x in range(2, n):
# #         if n % x == 0:
# #             print(f"{n} equals {x} * {n//x}")
# #             break

# # for n in range(2, 10):
# #     if n%2 == 0:
# #         print(f"{n} is even")
# #         continue
# #     else:
# #         print(f"{n} is odd")

# # while True:
# #     pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# #FUNCTIONS
# # def http_error(status):
# #     match status:
# #         case 400:
# #             return "Bad request"
# #         case 404:
# #             return "Not found"
# #         case 418:
# #             return "I'm a teapot"
# #         case _:
# #             return "Something's wrong with the internet"
# # print(http_error(404))  # Example usage

# #MATCH STATEMENT
# # def week(day):
# #     match day:
# #         case 0:
# #             return "Monday"
# #         case 1:
# #             return "Tuesday"
# #         case 2:
# #             return "Wednesday"
# #         case 3:
# #             return "Thursday"
# #         case 4:
# #             return "Friday"
# #         case 5:
# #             return "Saturday"
# #         case 6:
# #             return "Sunday"
# #         case _:
# #             return "Invalid day"
# # print(week(3))  # Example usage

# # def greet():
# #     print("Hello, welcome to the Python practice script!")
# # greet()  # Call the greet function to display the welcome message

# # def fib(num):
# #     a,b=0,1
# #     while a<num:
# #         print(a, end=" ")
# #         a, b = b, a + b
# #     print()  # Print a newline after the Fibonacci sequence
# # fib(1000)


# # my_tuple = ("apple", 10, 3.14, True)
# # print(my_tuple)  # Print the entire tuple
# # print(my_tuple[0])  # Access the first element of the tuple
# # my_tuple = my_tuple + ("banana", 20)  # Concatenate another tuple
# # print(my_tuple)  # Print the updated tuple
# # my_tuple[0]= "orange"  # Attempt to change the first element (will raise an error)
# # print(my_tuple)  # Print the tuple after attempting to change it


# #LAMBDA FUNCTION
# def make_increament(n):
#     return lambda x: x + n

# f= make_increament(42)
# print(f(0))  # Output: 42
# print(f(1))  # Output: 43

