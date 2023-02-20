# ken={"name":"brian",
# "colours":"blue"
# }

# print(ken["name"])
# #update dictionary
# ken.update ["name":"alex"]
# print(ken)

# #nested dictionary
# kenya={
#     "counties":["kisumu","nyeri","kiambu",]
# }
# light_theme=  {button:["red"]
#                 "titlle":["white"]


# #def
          
               
# }


# # variable(name=input("write your name: "))


# #adding of two integers
# num1=eval(input("enter a number"))#eval is used to change a string to a  an integer
# num2=eval(input("enter num2"))
# print(num1 + num2)

# cars={    "model":"ford" ,
#           "colour":"black",
#           "country":"germany",
#            "year": 1988     
# }


# person ={
#           "name":"cathy" ,
#           "age" : 23,
#           "pets"  :["dogs","cat"]
# }
# print(person["pets"])

# #integer keys

# teams ={1: "a",
#         2:"b",
#         3:"c"
# }
# teams[2]
# #creating akey values in an empty dictionary
# profile ={}
# profile["username"] ="user123"
# profile["age"] = 20
# profile["brand"] ="addidas"
# print(profile)
profile  ={}
def register():
    username =input("enter username:")
    email= input("enter email:")
    password =input("enter password:")

    profile["username"]=username
    profile["email"]=email
    profile["password"]=password

def get_profile():
    #print the user profile
    print(profile)

def change_username():
   new_username=input("enter new username")
   profile["username"]=new_username
register()
get_profile()    

change_username()
get_profile()
    #ask for username
    #ask for email
    #ask for password
#dictionary methods
# 1.clear
# 2.pop
# 3.keys
# 4.values
# 5.get
# 6.popitem
# 7.update