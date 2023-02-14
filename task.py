# numbers=[33,23,11,16,27,10,5,34,5]
# print(len(numbers))#1a

# print(numbers.pop(5))#1b
# #  
# print(numbers.reverse)#1c

#1e
# numbers.remove(5)
# numbers.remove(33)

# numbers.sort()
# print(len(numbers)) 
 
# for i in range(len(numbers)):
#   print(numbers[i]) 

  ##2a

# for res in range((1,100)):
#  print(res)

# import random
# # randomlist=[]
# # for i in range(0,5):

# # =random.randint(1,30)
# # randomlist.append(n)
# # print(randomlist)



# #task questions
# #1a
# num =[]

# generating random  numbers

from random import randint

nums = []
#generate alist of random numbers
for i in range(20):
  number=randint(1,100)
  nums.append(number)
  print(nums)

# for num in range(100):
#   if(num % 2 == 0):
#     nums.append(num)

# for i in nums:
#   print(nums[i])