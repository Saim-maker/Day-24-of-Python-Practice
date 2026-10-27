# numbers = [5, 12, 8, 25, 3, 18, 10, 30]
# list = []
# for number in numbers:
#     if number > 10:
#         list.append(number)
# print(list)
from enum import unique
from multiprocessing.reduction import duplicate

# numbers = [4, 2, 4, 7, 4, 9, 2, 4]
# target = 4
# count = 0
# for number in numbers:
#     if number == target:
#         count = count + 1
# print(count)

# numbers = [1, 3, 5, 7, 3]
# list = []
# for number in numbers:
#     if number not in list:
#         list.append(number)
#     else:
#         print("The list is not unique")

# numbers = [12, 45, 7, 89, 34, 56]
#
# largest = numbers[0]
# second_largest = None
#
# for number in numbers:
#     if number > largest:
#         second_largest = largest
#         largest = number
#     elif number != largest:
#         if second_largest is None or number > second_largest:
#             second_largest = number
#
# print("Largest:", largest)
# print("Second largest:", second_largest)


# numbers = [23, 56, 12, 89, 34, 67]
# largest_number = numbers[0]
# smallest_number = numbers[1]
# for number in numbers:
#     if number > largest_number:
#         largest_number = number
#     elif number < smallest_number:
#         smallest_number = number
# print(largest_number, smallest_number)

numbers = [15, 40, 25, 70, 55, 60]
largest = numbers[0]
second_largest_number = numbers[1]
for number in numbers:
    if number >= largest:
        largest = number
    elif number < largest:
        second_largest_number = number
print(largest)
print(second_largest_number)
