#The following input list can be updated
input_items=[[1,2,3,4,[5,[6,[7]],8, 6]]]

#Problem 1
#Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
#This is to be done with a while loop. Note: the input will contain only integers or lists. 
print("Problem 1")
#create a copy of the original input list
current_list=input_items
#while any item in the current list variable is a list
while any(isinstance(x, list) for x in current_list):
    #create an empty list variable
    nextlevel=[]
    #start index at 0
    i=0
#while we are at an index in the list
    while i < len(current_list):
        #if the item at that index is a list
        if type(current_list[i])==list:
            #extend the list into the new variable
            nextlevel.extend(current_list[i])
        #increment the index and rerun
        i=i+1
    #once we have run through all indexes, reset current list to next level so that the while loop runs over the new list, which should now be one level below the previous
    current_list=nextlevel
#now that we have the innermost nested values, we just need to add 1 to them
for i in range(len(nextlevel)):
    nextlevel[i]=nextlevel[i]+1
print(nextlevel)

#Problem 2
#Write the a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
#This is to be done with recursion. Note: the input will contain only integers or lists. 
print("Problem 2")
def plus1function(input_items):
#innermost function that calls this modifiable list
    def nested_list(input_items):
    #define empty list to capture results
        interim_input=[]
    #for index i in the input list
        for i in input_items:
    #if the item is a list
            if isinstance(i, list):
    #add the item to our empty list
                interim_input.append(i)
    #now we need to recurse to keep adding every list until we find the innermost, this runs over the function again with the smaller list
                interim_input.extend(nested_list(i))
            #now if we find that the item at index i is not a list, continue
            else: continue
        #our function returns every list in the list. To find the innermost, we just need to return the last item
        return interim_input
    #set a new variable to contain all of the lists in the original list. We know the innermost list is the last item in the list
    finalresult=nested_list(input_items)
    #set addone equal to the last list in the list
    addone=finalresult[-1]
    for i in range(len(addone)):
        addone[i]=addone[i]+1
    return addone
problem2solution=plus1function(input_items)
print(problem2solution)

#Problem 3
#Write a python program that, given an input list, will filter the input above a user defined threshold. 
#This is to be done with a standard function. That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), it should return [1,2,3,4,5,6]
#list to be filtered
print("Problem 3")
inputnums=[1,2,3,4,5,6,7,8,9,1,1]
#user argument to be updated
filterselection=6
#function starts here
def lessthanfunction(inputnums):
    #create an empty list to hold our ultimate output
    filteredlist=[]
    #if value at i is less than filterselection
    for i in range(len(inputnums)):
        if inputnums[i]<=(filterselection):
            #append the value at the index to the empty list
            filteredlist.append(inputnums[i])
        #if i is out of range, continue
        else: continue
    return filteredlist

problem3solution=lessthanfunction(inputnums)
print(problem3solution)


