#second python list
numbers=[23,43,44,56,78,87]
name=("java","c++","go","rust",)
print(len(numbers))#used to get the numbers of elements in the list of numbers

for i in range(len(numbers)):
    print(numbers[i])#code prints the list of numbers

for x in range(len(name)):
    print(name[x])#prints the list of names

  #LIST METHODS

    #INDEX

print(numbers.index(78))#used in getting position of an element in alist
print(name.index("go")) #code used in getting position of an element in alist

#appending-his is adding an element at the end of a list

# BEFORE APPENDING
# for i in range(len(numbers)):
    # print(numbers[i])
#the appending code of a number element in alist
numbers.append(90) 
print(numbers)

#there is an error in appending a name in the name list
# for i in range(len(name)):t
    # print(name[i])

# print("\n")
# name.append("javascript")
# print(name)

#sorting-this is arranging a list of integers in ascending order
numbers.sort()

#count-this gives the number of times an element appears in a list
print(numbers.count(23))

#pop-removing and returning an element in a list
# print(numbers.pop(2))

#insert-introduces an element x at an index y in a list
# numbers.insert(3,300)

# for i in range (len(numbers)):
    # print(numbers[i])

#remove-removes the first occurrence of an element from a list
numbers.remove(44)

# for i in range(len(numbers)):
    # print(len(numbers))

numbers.remove(23)


# # #TIPS AND  TRICKS

#multipliying a number increasing the times it appears in a list

three=[3]*10

#joining two lists together

list1=[45,554,445,33,66,77]
list2=[65,66,83,11]
final_list=list1+list2
print(final_list)

#slicing a list

#getting the integer with the highest value in the list
num=[44,33,12,14,33,56,73]
max(num)

#the minimum value
min(num)#gives the number with least value in the list

#creating an empty list
nums=[]#the  empty list

for i in range(10):

    nums.append(i)

for i in range(len(nums)):
    print(nums[i])

#exercises
even_nums=[] 
for num in range(100):
    if(num % 2 ==0):
        even_nums.append(num)

for i in even_nums:
    print(even_nums[i]) 
