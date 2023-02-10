#my python list
name=["john","james"]
numbers = [34,45,54,55,33,34]
#print(len(numbers)) # get the length on my list

#for i in range(len(numbers)):
#   print(numbers[i])

#LIST METHODS
#Index
#print(numbers.index(55))

#append- add an element to the end

#before appending
#for i in range(len(numbers)):
   #print(numbers[i])

#print(name)
numbers.append(67)
#print(numbers)
#sort
#count
#pop
#nsert
numbers.insert(2,100)
for i in range(len(numbers)):
   print(numbers[i])
#tips and tricks
#multiplying a list
fives =[5]* 5
fives
#slicing alist
#creating a list
nums=[] #empty list
for i in range(10):
   #insert elements into the list
   nums.append(i)

for i in range(len(nums)):
   print(nums[i])

even_nums=[]

for num in range(20):
   if (num % 2 == 0):
       nums.append(num)

for i in range(len(nums)):
   print(nums[i])