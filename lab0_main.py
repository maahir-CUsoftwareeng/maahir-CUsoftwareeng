
#Any and all import statements
import lab0_functions

#Exercise 1
#Step 1: Q) What is displayed when Python evaluates point1 (  >>>point1 = [13.0, 12.0]  ) ?
#A) [13.0, 12.0]

#Step 2: Q) Are lists mutable? A) Yes
#>>> point1.append(4.0) 
#>>> point1
#    [13.0, 12.0, 4.0]   4.0 has been added to the list

#What is displayed each time Python evaluates point1?
#>>> point1.pop(0)  # Remove the item at index 0 in the list 
#    13.0
#>>> point1 
#    [12.0, 4.0]

#>>> point1.pop()   # Remove the last item in the list
#    4.0
#>>> point1
#    [12.0]

#Step3
# What is displayed when the last two statements are evaluated? (Steps to create a tuple)
#>>> point1 = (13.0, 12.0)  The paranthesis are OPTIONAL
#>>> type(point1)
#    <class 'tuple'>
#>>> point1
#    (13.0, 12.0)

#Step 4
#What is displayed when Python evaluates x and y?
#>>> x = point1[0] 
#>>> y = point1[1] 
#>>> x 
#    13.0
#>>> y 
#    12.0

#What is displayed when Python evaluates x and y?
#>>> point2 = (14.0, 16.0) 
#>>> x, y = point2 
#>>> x 
#    14.0
#>>> y
#    16.0

#Step 5
#Q) Are tuples immutable? A) Yes
#>>> point2[0] = 12.0     # Can we change the point to (12.0, 16.0)? 
#Traceback (most recent call last):
#  Python Shell, prompt 24, line 1
#builtins.TypeError: 'tuple' object does not support item assignment

#>>> point2.append(4.0)  # Can we add a third coordinate? 
#Traceback (most recent call last):
#  Python Shell, prompt 25, line 1
#builtins.AttributeError: 'tuple' object has no attribute 'append'

#>>> point2.pop(0)       # Can we remove the first coordinate?
#Traceback (most recent call last):
#  Python Shell, prompt 26, line 1
#builtins.AttributeError: 'tuple' object has no attribute 'pop'

#Step 6 
# Q) Can we create a list of tuples? A) Yes, and it may be useful at times to do so
#>>> points = [(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)] 
#>>> points[0] 
#    (1.0, 5.0)
#>>> points[1] 
#    (2.0, 8.0)
#>>> points[2]
#    (3.5, 12.5)

#Exercise 2
test1=lab0_functions.max_min([(27, 219, 134, 12)])
test2=lab0_functions.max_min([(27, 219, 134, 12),(900,3,20,68)])
test3=lab0_functions.max_min([(434,253,53,6),(31,54,76,234),(21,35,658,57)])
print(test1)
print(test2)
print(test3)

#Exercise 3
#Step 1 Q) Can sets contain tuples? A) Yes, because they are immutable
#>>> points = {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)} 
#>>> points
#    {(10.0, -2.0), (1.0, 2.0), (4.0, 6.0)}

#>>> point1 = (1.0, 2.0) 
#>>> point2 = (4.0, 6.0) 
#>>> point3 = (10.0, -2.0) 
#>>> points = {point1, point2, point3} 
#>>> points
#    {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}

#>>> points = set() 
#>>> points.add(point2) 
#>>> points.add(point3) 
#>>> points
#    {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}

#Step 2
#>>> points.add(point2) 
#>>> points
#    {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}
#Q) How many copies of point (4.0, 6.0) are in the set? A) Only 1 because the items in a set do not repeat

#Step3 
#Q) Can individual points in the set be retrieved by specifying an index (position)? A) No
#>>> point[0]
#    Traceback (most recent call last):
#  Python Shell, prompt 16, line 1
#builtins.TypeError: 'set' object is not subscriptable

#Step 4
#>>> for point in points: 
#...     print(point) 
#...
#    (4.0, 6.0)
#    (1.0, 2.0)
#    (10.0, -2.0)

#Exercise 4
test_1=lab0_functions.sum_y({(5.60,4.90),(3.35,8.29),(-9.67,3.29)})
test_2=lab0_functions.sum_y({(29.06,-394.0),(23.345,454.786),(-2003.48,513.0492),(123.543,675.2545)})
test_3=lab0_functions.sum_y({(3.466,3804.6),(3.466,3804.6),(-243.76,53.312),(-413.47,324.865)})
print(test_1)
print(test_2)
print(test_3)
