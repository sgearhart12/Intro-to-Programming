print("Problem 1a")
arg1 = [1,2,3]
arg2 = [1,1,1]
def wrong_add_function(arg1,arg2):
   arg1_index=0
   while arg1_index < len(arg1):
      print("At the beginning we have arg1=", arg1, "and arg2 =", arg2)
      #confirmed using print that this is looping through three indexes. When I updated the argument, the indexes increased accordingly.
      arg_2_sum = 0
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
         print("Value of arg_1 inside of the loop:", arg1)
         print("Value of arg2 inside of the loop:", arg2)
         #now we see that for index 0 we have value of 6, index 1 value of 9, index 2 value of 12 for arg_2_sum.
         #we see that only arg1 is changing.
         #when index=0, (1+i for i in arg2) which is sum(1+0, 1+1, 1+2)=6
         #when index=1 (2+i for i in arg2) which is sum(2+0, 2+1, 2+2)=9
         #when index=2 (3+1 for i in arg2) which is sum(3+0, 3+1. 3+2)=12
      print("Arg2 sum is equal to", arg_2_sum)
      arg1[arg1_index]=arg_2_sum  
      print("Value of arg1 outside of the loop:", arg1)
      #now we can see that arg1 is set to the sum, rather than each index number being added. Then the loop repeats with the new value for arg1[0]
      arg1_index+=1
   print(f"Final value arg1={arg1} and final value arg2={arg2}")
   return arg1
wrong_add_function(arg1, arg2)
#Questions
#How do we use print to better point out the exact issue with the code rather than just returning the values in different locations?
#Unclear based on the description of what the function is supposed to do whether we are supposed to add each index element together or sum list b and add this value to each vlaue in list a.
#I don't understand what I need to output into a single variable.

print("Problem 1b")
#Assuming that the goal of the function is to sum list b and add this number to each value in list a
arg1 = [1,2,3]
arg2 = [1,1,1]
def correct_add_function(arg1, arg2):
   arg1_index=0
   while arg1_index < len(arg1):
      print("Value og arg1=", arg1, "and value of arg2=", arg2)
      arg1[arg1_index]=arg2[arg1_index]+arg1[arg1_index]  
      print("Value of arg1 in the loop:", arg1)
      print("Value of arg2 in the loop:", arg2)
      arg1_index+=1
   return arg1
correct_add_function(arg1, arg2)
print(arg1)