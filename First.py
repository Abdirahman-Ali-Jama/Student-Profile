# Q1
x = 5
y = "5" 
print(x + int(y) * 2) # this will print 15 because
# y is converted to an integer and then multiplied by 2 before being added to x.

# Q2
x = 10
y = x
x = x + 5
y = y * 2
print(x, y) # this will print 15 and 20 because x is updated to 15 and y is updated to 20
# based on the original value of x which was 10

# Q3
data = ["Python", 3, 8.5] 
a, b, c = data 
print(a * b) # this will print "PythonPythonPython" because a is "Python" and b is 3,
# so when we multiply them, it repeats the string "Python" three times.

# Q4
x = 10
y = "20"
print(x + int(y)) # this will print 30 because y is converted to an integer and then added to x
# way 2 concatination
print(str(x) + y) # this will print "1020" because x is converted
# to a string and then concatenated with y which is already a string.

# Q5
x = "Hello" 
def change(): 
    x = "World" 
change() 
print(x) # this will print "Hello" because the variable x inside the function change() is a local variable
# and does not affect the global variable x outside the function.

# Q6
print("Age:", 20 + 5, "Years" + " Old") # this will print "Age: 25 Years Old" because the first part is a string, 
# the second part is an integer that gets evaluated to 25, and 
# the third part is a string that gets concatenated with " Old".

# Q7
x = y = z = 10 # All variables x, y, and z are assigned the value 10
x += 5 # x is updated to 15
y *= 2 # y is updated to 20
z -= 3 # z is updated to 7
print(x, y, z) 

# Q8
age = 25
Age = 30
print(age + Age) # the output will be 55 b/c python is case-sensitive,
# so age and Age are treated as two different variables.

# Q9
fruits = ["apple", "banana"] 
# x, y, z = fruits
print(x, y, z) # Match variables with list length: Ensure that the number of variables matches the number of items in the list.
# In this case, we can add a third variable to match the length of the list.
fruits = ["apple", "banana", "orange"]
x, y, z = fruits
print(x, y, z) # this will print "apple", "banana", and "orange" because now we have three variables to unpack the three items in the list.

# Q10
x = "3" 
y = 2 
z = float(x) * y + int(x) 
print(z) # this will print 9.0 b/c the string "3" is converted to a float (3.0) and then multiplied by 2 to get 6.0,
# and then the string "3" is also converted to an integer (3) and added to 6.0 to get 9.0.

# Q11
print("Hello", end="-") 
print("World", end="-") 
print("Python") # this will print "Hello-World-Python" because the end parameter in the print function specifies what to print at the end of the output.

# Q12
x = "10" 
y = "5" 
print(int(x) + int(y) * int(x)) # this will print 60 because the string "10" is converted to an integer (10) and the string "5" is converted to an integer (5),
# so the expression becomes 10 + 5 * 10, which is evaluated as 10 + 50, resulting in 60.

# Q13
x = 5 # initial value of x
x = x + 2 # x is updated to 7
x = x * x # x is updated to 49
x = x - 3 # x is updated to 46
print(x) # this will print 46 because the variable x is updated step by step according to the operations performed on it

# Q14
my_var = 10 
myVar = 20 
print(my_var + myVar) # there is no error in this code because Python is case-sensitive, so my_var and myVar are treated as two different variables.

# Q15
x, y = 5, 10 # x is assigned 5 and y is assigned 10
x, y = y, x + y # swapping values: x is updated to the value of y (10) and y is updated to the sum of the original x and y (5 + 10 = 15)
print(x, y ) # this will print 10 and 15 because after the swap, x takes the value of y (10) and y takes the value of the original x plus y (5 + 10 = 15).

