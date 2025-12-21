# list = ["himanshu","mohit","sachin","priyanshu","himanshu"]
# # print(list.count("himanshu"))
# list.append("new_user")
# print(list)
# list.insert(2, 45)
# print(type(list))
# print(list)
# Pop = list.pop(2)
# print(Pop)
# print(list)

# list.remove("himanshu")
# print(list)


# # LIST AS A STACK
# stack = []
# stack.append("A")
# stack.append("B")  
# stack.append("C")
# print(stack)
# print(stack.pop())  # Removes and returns the last item
# print(stack)


# LIST AS A QUEUE
# from collections import deque
# queue = deque(["A", "B", "C"])
# queue.append("D")
# print(queue)  # Add to the end of the queue
# print(queue.popleft())  # Remove and return the first item
# print(queue.popleft())  # Remove and return the next item
# print(queue)  # Remaining items in the queue


# LIST COMPREHENSION
#1st way
# squares = [x**2 for x in range(10)]
# print(squares)

#2nd way
# squares =  []
# for x in range(10):
#     squares.append(x**2)
# print(squares)

#nested list comprehension
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]