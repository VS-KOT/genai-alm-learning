'''almost same as c++'''
'''def keyword is used for function definition'''
'''pass keyword is used to declare a function without any code incase if no code or writing code in future'''
def emptyfunction():
    pass

emptyfunction()
print(emptyfunction)    #returns address
print(emptyfunction())  #returns None as there is no output value

name = "vinayak"
print("Hello {} ".format(name))

'''args and kwargs'''
'''there can be multiple arguments passed when using these two. If the variable is declared then args is used and stored as tuple and kwrgs for undeclared values and stored a dictionary'''

def student_info(*args, **kwrgs):
    print(args, type(args))
    
    print(kwrgs, type(kwrgs))

student_info("Math", "Science", 44,  student_name = "Vinayak", Age = 22)   #all positional arguments must come before keyword arguments


'''If any sequence or dictionary are passed in args/kwrgs with star(*) then those values will be passed individually '''

courses = ["Biology", "Chemistry", "Maths"]
course_info = {"teacher": "ABC", "desig": "DEF", "salary": 5656}

student_info(courses, course_info)      #no unpacking of values and passed as seperate values
student_info(*courses, **course_info)   #unpack values and pass as individually