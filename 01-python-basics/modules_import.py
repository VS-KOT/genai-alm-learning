# modules_import & modules_export are linked 
# module_export can be easily imported as they both are in same directory

import modules_export as me   #whole module gets imported
from modules_export import addition as addi  # only a Function is imported. This will not be loaded seperately here because the whole module is already imported before. Access to local variables in export file will be given only if mentioned seperately while calling the importing the function

from modules_export  import * #import everything but considered a bad practice as difficult to track
 
import random 
import datetime   #Just for todays date and time
import calendar   #addition operations such as isleap() to check if year is leap or not

import os        #access to current operating system, access to create file, delete files.
import antigravity


#actually while importing python is able to find the actual path of the file without user provided details and this is possible because of sys.path (system path) file

'''sys file contains paths :
 1. current file 
 2. python path environment variables
 3. standard library path
 4. Third party packages path
'''
'''
 if the file is in other path/directory from the mentioned above then you will have to add manually
 import sys then sys.path.append('path') or the better practice is to add the path in local environment variables
'''

print(addi(3,40))

courses = ["science", "english", "maths", "arts"]
str = "arts"
print("index is ", me.findStr(courses, str))


print(random.choice(courses))   #chooses random value from the courses list
print(datetime.datetime.now())
print(calendar.isleap(datetime.datetime.now().year))


print(os.getcwd())  #gives current working directory



#all the modules are python files themselves and to check the configuration/path of the file are in dunder file represented by (__file__)
print(os.__file__)
antigravity



