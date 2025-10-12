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
   return arg1, arg2
wrong_add_function(arg1, arg2)

print("Problem 1b")
#Assuming that the goal of the function is to add each index item in list b to each index item in list a, here is a corrected version.
arg1 = [1,2,3]
arg2 = [1,1,1]
def correct_add_function(arg1, arg2):
   arg1_index=0
   while arg1_index < len(arg1):
      print("Value og arg1=", arg1, "and value of arg2=", arg2)
      #add corrected syntax here so that each element is added together.
      arg1[arg1_index]=arg2[arg1_index]+arg1[arg1_index]  
      print("Value of arg1 in the loop:", arg1)
      print("Value of arg2 in the loop:", arg2)
      arg1_index+=1
   return arg1, arg2
correct_add_function(arg1, arg2)

print("Problem 2a")
#replacing the numeric section with my corrected code from the previous problem.
arg_str_1=["1","2","3"]
arg_str_2=["1","2","3"]

def wrong_add_function(arg_str_1, arg_str_2):
   arg1_index=0
#numeric section
#the following if statement will not run if arg1 or arg2 contain non-integers
   if sum([type(i)==int for i in arg_str_1])==len(arg_str_1) and \
      sum([type(i)==int for i in arg_str_2])==len(arg_str_2):
      print("Enters numeric section")
      while arg1_index < len(arg_str_1):
         arg_str_1[arg1_index]=arg_str_2[arg1_index]+arg_str_1[arg1_index]
         arg1_index+=1
      return arg_str_1
#string section
#the following if statement will not run if arg1 or arg2 contain non-strings
   if sum([type(i)==str for i in arg_str_1])==len(arg_str_1) and \
      sum([type(i)==str for i in arg_str_2])==len(arg_str_2):
      arg1_index=0
      while arg1_index < len(arg_str_1):
         arg_2_sum = ''
         for arg2_elements in arg_str_2:
            arg_2_sum += arg2_elements
            arg_str_1[arg1_index]=arg_str_1[arg1_index]+str(arg_2_sum)
         arg1_index+=1
      return arg_str_1, arg_str_2
wrong_add_function(arg_str_1, arg_str_2)
problem2a=wrong_add_function(arg_str_1, arg_str_2)
print(problem2a)

arg_str_1=["1","2","3"]
arg_str_2=["1","2","3"]
#for problem 2b, my first instinct was to add else since the if statements were not being entered. I've left my code here. 2b2 shows the try/except statement version.
print("Problem 2b1")
def additional_add_function(arg_str_1, arg_str_2):
   arg1_index=0
#numeric section
#the following if statement will not run if arg1 or arg2 contain non-integers
   if sum([type(i)==int for i in arg_str_1])==len(arg_str_1) and \
      sum([type(i)==int for i in arg_str_2])==len(arg_str_2):
      print("Enters numeric section")
      while arg1_index < len(arg_str_1):
         arg_str_1[arg1_index]=arg_str_2[arg1_index]+arg_str_1[arg1_index]
         arg1_index+=1
      return arg_str_1
#string section
#the following if statement will not run if arg1 or arg2 contain non-strings
   if sum([type(i)==str for i in arg_str_1])==len(arg_str_1) and \
      sum([type(i)==str for i in arg_str_2])==len(arg_str_2):
      arg1_index=0
      while arg1_index < len(arg_str_1):
         arg_2_sum = ''
         for arg2_elements in arg_str_2:
            arg_2_sum += arg2_elements
            arg_str_1[arg1_index]=arg_str_1[arg1_index]+str(arg_2_sum)
         arg1_index+=1
      return arg_str_1
   #added an else statement since the two ifs are being skipped when we have mixed lists as arguments
   else:
      print("Neither numeric or string section entered")
      try:
         sum(arg_str_1)
      except(TypeError, ValueError, IndexError):
         print("Your input argument has a type mismatch")
         for i in range(len(arg_str_1)):
            if type(arg_str_1[i])==str:
               print(f'Your input for arg1 is a string at position {i}, please change to all strings or all integers to proceed')
      try:
         sum(arg_str_2)
      except(TypeError, ValueError, IndexError):
         print("Your input argument has a type mismatch")
         for i in range(len(arg_str_2)):
            if type(arg_str_2[i])==str:
               print(f'Your input for arg2 is a string at position {i}, please change to all strings or all integers to proceed')
additional_add_function(arg_str_1, arg_str_2)
problem2b1=additional_add_function(arg_str_1, arg_str_2)
print(problem2b1)

arg_str_1=["1","2","3"]
arg_str_2=["1","2","3"]
#here is the version using try/except
print("Problem 2b2")
def exception_add_function(arg_str_1, arg_str_2):
   try:
      #first line will pass if list types are all int, second line will pass if they are all str
      if all(isinstance(x,int) for x in arg_str_1) and all(isinstance(x,int) for x in arg_str_2):
         print("No issue in type, all integers") 
         return(wrong_add_function(arg_str_1, arg_str_2))  
      if all(isinstance(x, str) for x in arg_str_1) and all(isinstance(x,str) for x in arg_str_2):
         print("No issue in type, all string")
         return(wrong_add_function(arg_str_1, arg_str_2))
      #if the above are skipped for not being true, we know there is a type mismatch. Now we can intentionally throw an error
      else: sum(arg_str_1) and sum(arg_str_2)
   except(TypeError, ValueError, IndexError):
      print("Your input argument has a type mismatch")
      for i in range(len(arg_str_1)):
         if type(arg_str_1[i])==int:
            print(f'Your input for arg1 is an integer at position {i}, please change to all strings or all integers to proceed')
      for i in range(len(arg_str_2)):
         if type(arg_str_2[i])==int:
            print(f'Your input for arg2 is an integer at position {i}, please change to all strings or all integers to proceed') 
      for i in range(len(arg_str_1)):
         if type(arg_str_1[i])==str:
            print(f'Your input for arg1 is a string at position {i}, please change to all strings or all integers to proceed') 
      for i in range(len(arg_str_2)):
         if type(arg_str_2[i])==str:
            print(f'Your input for arg2 is a string at position {i}, please change to all strings or all integers to proceed') 
exception_add_function(arg_str_1, arg_str_2)   
problem2b2=exception_add_function(arg_str_1, arg_str_2)
print(problem2b2)

arg_str_1=["1","2","3"]
arg_str_2=["1","2","3"]
print("Problem 2c")
def correction_add_function(arg_str_1, arg_str_2):
   try:
      #first line will pass if list types are all int, otherwise will skip
      if sum([type(i)==int for i in arg_str_1])==len(arg_str_1) and \
      sum([type(i)==int for i in arg_str_2])==len(arg_str_2):
         return wrong_add_function
      #first line will pass if list types are all str, otherwise will skip
      if sum([type(i)==str for i in arg_str_1])==len(arg_str_1) and \
      sum([type(i)==str for i in arg_str_2])==len(arg_str_2):
         #create a new variable to hold our corrected list
         newoutput=[]
         for i in range(len(arg_str_1)):
         #the following code will take the first slice of the object at each list index in arg1 and add the whole of arg2 to it
            newoutput.append((str(arg_str_1[i])[0])+"".join(arg_str_2))
            return newoutput
      else: 
      #if the if and elif were skipped, we know there is a type mismatch in the list. Intentionally create an error
         sum(arg_str_1) and sum(arg_str_2)
   except(TypeError, ValueError, IndexError):
      print("Your input argument has a type mismatch")
      for i in range(len(arg_str_1)):
         if type(arg_str_1[i])==int:
            print(f'Your input for arg1 is an integer at position {i}, please change to all strings or all integers to proceed')
      for i in range(len(arg_str_2)):
         if type(arg_str_2[i])==int:
            print(f'Your input for arg2 is an integer at position {i}, please change to all strings or all integers to proceed') 
      for i in range(len(arg_str_1)):
         if type(arg_str_1[i])==str:
            print(f'Your input for arg1 is a string at position {i}, please change to all strings or all integers to proceed') 
      for i in range(len(arg_str_2)):
         if type(arg_str_2[i])==str:
            print(f'Your input for arg2 is a string at position {i}, please change to all strings or all integers to proceed') 
   
problem2solution=correction_add_function(arg_str_1, arg_str_2)
print(problem2solution)

