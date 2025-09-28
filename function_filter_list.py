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