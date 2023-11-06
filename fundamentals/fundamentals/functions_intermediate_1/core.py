#1 Update Values in Dictionaries and Lists
   #Change the value 10 in x to 15

x = [ [5,2,3], [10,8,9] ] 
x[1] [0] = 15
print(x)
   
   #Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students [0] ["last_name"] = "Bryant"
print(students)

   #In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
["soccer"] [0] = "Andre"
print(sports_directory)

   #Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
z[0] ["y"] = 30
print(z)

#2 iterate through a list of dictionaries
def iterateDictionary(list):
    for i in range (0,len(list)):
    # print(list[i])
        output = ""
        for [key,value]in list[i]:
            output = f" key - value"
            print(output)


#3 Get Values From a List of Dictionaries
def  iterateDictionary2(key_name, some_list):
    for i in range (0,len(list)):
        for key,value in list [i]:
            if key == key_name:
              print(value)

#4 Iterate Through a Dictionary with List Values
def printInfo(dic):
    for key,value in dic.items:
        print (f" {len(value)}, {key.upper()}")
        for i in range (0,len(value)):
            print(value[i])

    

