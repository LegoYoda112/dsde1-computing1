'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>
def welcome_message(user_name = None, place = None):
    name_string = ''
    if user_name != None:
        name_string = ', ' + user_name + ','

    place_string = ''
    if place != None:
        place_string = ' to ' + place

    return_string = 'Hello' + name_string + ' and welcome' + place_string
    return return_string

# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list
def unique(input_list):
    unique_list = []
    for number in input_list:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list

def secondTuple(input_tuple):
    return input_tuple[1]

def list_average(list, avg_type = 'mean'):

    if avg_type == 'mode':
        counted_list = []

        unique_list = unique(list)

        for number in unique_list:
            counted_list.append((number, list.count(number)))
        
        counted_list = sorted(counted_list, key = secondTuple, reverse = True)
        
        return_list = []
        max_count = counted_list[0][1]
        print(max_count)

        for counted_pair in counted_list:
            number, count = counted_pair

            if(count < max_count):
                break 

            return_list.append(number)
            
        return return_list

    if avg_type == 'mean':
        list_sum = 0.0
        for number in list:
            list_sum += number
        return list_sum/len(list)

    if avg_type == "median":
        sorted_list = sorted(list)
        return sorted_list[int(len(list)/2)]