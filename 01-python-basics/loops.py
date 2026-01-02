'''for-in loop -> inbuilt new line character'''
courses = ["abc","def","ghi","jkl"]
for course in courses:
    print(course) 

'''enumerate function -> if in a list you want to access element along with index then you can create a variable in loop with enumerate function '''
'''enumerate return 2 values -> index and value'''
for index, course in enumerate(courses):
    print(index, course)

'''you can also pass the intial value of index if you want'''
for index, course in enumerate(courses, start= 2):
    print(index, course)