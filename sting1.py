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

string="toyota"
print(string.upper())
print(string.lower())

#checking for alphanumeric
x="string123"
print(x.isalpha())



#password
password="latent233"
if password.isalpha():
    print("invalid password")
else:
    print("valid password")    


name2="hello"
name1=input("ask for username")
print(name2+ name1.upper())

