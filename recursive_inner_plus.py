#The following input list can be updated
input_items=[[1,2,3,4,[5,[6,[7]],8, 6]]]
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