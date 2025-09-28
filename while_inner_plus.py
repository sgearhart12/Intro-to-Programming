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