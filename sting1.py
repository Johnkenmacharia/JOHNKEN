name ="climate"

#index
print(name[0])

print(name[-1])

for letter in name:
    print(letter)

print()

print("-"*5)

# "s"+"t"+"r"+"i"+"n"+"g"

# a="hello"
# b= "kamau"
# print(a+b)
# #
# name1=input("enter a name:")
# name2="hello"
# print("hello"+name1)

# #string method
# #upper -coverts from lower case to upper case

# string="toyota"



#password
password="latent233"
if password.isalpha():
    print("invalid password")
else:
    print("valid password")    


# name2="HELLO"
# name1=input("ask for username")
# print(name2+ name1.upper())


#1-program that ask user to enter a string

game=input("enter a string")
#gives the number of characters in a string
print(len(name))
#rewrites a string anumber of times 
print(game*3)
#writing the first character of a string
print(game[0])
#program that shows the first three characters of a string
#slicing
print(game[0:3])
#wtritng the last three characters
print(game[-3: ])
#program that shows a string in reverse
print(game[::-1])
#program that prints the seventh character
print(game[7])
#program that removes the first and the last characters of a string
print(game[1:-1]) 
#program  that erites a string in capital letters
print(game.upper())
#program that replaces every a character in a string with another character in  
# #a string
# string1=input("enter a string")
# ch=input("enter your own character")
# newch=input("enter new character") 

# string2=""
# for i in range(len(string1)):
#     if(string1[i]==ch):
#         string2

string1=game
string1.replace('a','e')

#2 a way of estimating the  of words in astring and the spaces and which user input a string
character=input("enter a string:")

print(len(character))

count=0
line=character
for i in line:
    if(i.isspace()):
        count=count +1
        print("the number of blank spaces is:",count)  

#3        
