# --- Day 4: Secure Container ---

# You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

# However, they do remember a few key facts about the password:

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these criteria?

# Your puzzle input is 367479-893698.

# input = [3, 6, 7, 4, 7, 9, 8, 9, 3, 6, 9, 8]

# input.sort()

# print ("The sorted list is : " +  str(input))

# dedup = [] 
# for i in input: 
#     if i not in dedup: 
#         dedup.append(i) 

# print ("The list after removing duplicates : " + str(dedup))


# print ("\n" "This is a WIP so I will continue on this one soon...")  

# This one does a lot of things but it isn't complete yet.
# import copy

# input = [3, 6, 7, 4, 7, 9, 8, 9, 3, 6, 9, 8]

# input.sort()

# def combinations(target,input):
# 	for i in range(len(input)):
# 		new_target = copy.copy(target)
# 		new_data = copy.copy(input)
# 		new_target.append(input[i])
# 		new_data = input[i+1:]
# 		print new_target
# 		combinations(new_target,
# 			new_data)

# target = []

# combinations(target,input)

# from itertools import combinations

# input = [3, 6, 7, 4, 7, 9, 8, 9, 3, 6, 9, 8]

# input.sort()

# print("The original list is: " + str(input))

# res = [] 
# for sub in range(6): 
#     res.extend(combinations(input, sub + 1))

# print("The combinations of elements till length N : " +  strc(res))


#function to return true if adjacent duplicate numbers
# def findDupes(num1):
#     value = False
#     array1 = list(str(num1))
#     for x in range(0,5):
#         if(array1[x]==array1[x+1]):
#             value = True
#             break
#     return value

# #function to return true if non-decreasing adjacent numbers
# def findDown(num1):
#     value = True
#     array1 = list(str(num1))
#     for x in range(0,5):
#         if(array1[x]>array1[x+1]):
#             value = False
#             break
#     return value

# count = 0;

# #loop to run through the range
# for i in range(183564,657475):
#     if(findDupes(i) and findDown(i)):
#         count += 1

# print("The number of possible correct passwords is: " + str(count))

from collections import Counter

input = '367479-893698'
lo, hi = [int(x) for x in input.split('-')]


def f(A):
    flag = False
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            return False
        if A[i] == A[i-1]:
            flag = True
    return flag



def g(A):
    D = Counter(A)
    if 2 in D.values():
        return True
    return False

cnt = 0
nums = []

for i in range(lo, hi+1):
    if (f(str(i))):
        nums.append(str(i))
        cnt += 1

print(cnt)

cnt2 = 0

for i in range(len(nums)):
    if g(nums[i]):
        cnt2 += 1

print(cnt2)