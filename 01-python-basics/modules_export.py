# modules_import & modules_export are linked 
# Module definition is here and it can be exported directly as the import is in same directory
#Remember that once the module is loaded it is executed completely before and then only the control goes back to original file where it is imported. So the last print statement will execute before and then function execution will be done in file it is imported 


print("Module is getting imported")

def findStr(strCollection, target):
    for i, value in enumerate(strCollection):
        if(value == target):
            return i
    
    return -1

def addition(a,b):
    return a+b


print("Module is completely executed")


