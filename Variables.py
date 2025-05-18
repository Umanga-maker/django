# # def myfunction():
# #     a = 10
# #     b = 20
# #     print ("variable a:",a)
# #     print ("variable b:",b)
# #     return a + b

# # print (myfunction())

# #global variables
# name = 'TutorialsPoint'
# marks = 50
# result = True
# def myfunction():
#     #accessing inside the function
#     print("name:",name)
#     print("marks:",marks)
# #function call
# myfunction()
# print(globals())

# def yourfunction():
#     a = 5
#     b = 6
#     #nested function
#     def myfunction():
#         #nonlocal function
#         nonlocal a
#         nonlocal b
#         a = 10
#         b = 20
#         print("variable a:",a)
#         print("variable b:",b)
#         return a+ b
#     print(myfunction())
# (yourfunction())


# name = 'TutorialsPoint'
# marks = 50
# result = True
# def myfunction():
#     a = 10
#     b = 20 
#     c = a + b
#     print(globals())
#     print ("locals():",globals)


#this is a global variable
marks = 50
def myfunction():
    marks = 70 #this is a local variable
    print (marks)

myfunction()
print (marks) #prints global value





