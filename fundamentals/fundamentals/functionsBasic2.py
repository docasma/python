#1 countdown
def countdown(num):
    output = []
    for i in range(num,-1,-1):
        output.append(i)
    return output
print(countdown(5))

#2 Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))


#3 First Plus Length
def first_plus_length(list):
    return list[0] + len(list)

print( first_plus_length ([4,5,8,9]))

#4 Values Greater than Second 
def values_greater_than_second (list):
    if len(list) < 2:
     return False
    new_list = []
    second_element = list[1]
    for number in list:
        if number > second_element:
            new_list.append(number)
    print (len(new_list))
    return new_list
result = values_greater_than_second ([5,4,6,8,9])
print(result)

# This Length That Value
def length_value (size,value):
    output = []
    for i in range (0,size):
        output.append(value) 
    return output  
print(length_value(5,8))




