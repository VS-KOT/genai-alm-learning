#Dictionaries#

'key-value pair'
dict_example = {'a':1, 'b':2 , 'c':3 , 'd':4, 'e':5}
print(dict_example['a'])

'''key can be of different types within same dictionary'''

'''if key doesn't exists then there will be an error'''
'''but if instead of error you want None you can use get method'''
'''and if you want some message if key is not found then pass a parameter in get'''

print(dict_example.get('d', "Not Found"))


'''if you want to add/modify value of multiple keys at a single time then use update method'''
dict_example.update({'a':5, 'phone':66666})
print(dict_example)


'''delete a value'''
del dict_example['phone']
print(dict_example)
deleted_elem = dict_example.pop('a')
print(dict_example, deleted_elem)


'''return all the keys as list, same as keys and items(keys and values)'''
print(dict_example.keys())


