# Function definition for Exercise 2
def max_min(lst: list)->list:
    """Returns the maximum and minimum value from each four item non-negative integer tuple in the input list "lst" and returns it as a list of tuples in the same order as the list input
  
    >>> max_min([(27, 219, 134, 12)])  
    [(219, 12)]
    >>> max_min([(27, 219, 134, 12),(900,3,20,68)]) 
    [(219, 12), (900, 3)]
    >>> max_min([(434,253,53,6),(31,54,76,234),(21,35,658,57)])
    [(434, 6), (234, 31), (658, 21)]
    """
    lst_out=[]
    for t in lst:
        a,b,c,d=t
        maximum=max(a,b,c,d)
        minimum=min(a,b,c,d)
        t_out=(maximum,minimum)
        lst_out.append(t_out)
    return lst_out

# Function definition for Exercise 4
def sum_y(points: set)->float:
    """Returns the sum of all the y coordinates from each of the tuples/coordinates from the input set "points" 
  
    >>> sum_y({(5.60,4.90),(3.35,8.29),(-9.67,3.29)})
    16.48
    >>> sum_y({(29.06,-394.0),(23.345,454.786),(-2003.48,513.0492),(123.543,675.2545)})
    1249.0897
    >>> sum_y({(3.466,3804.6),(3.466,3804.6),(-243.76,53.312),(-413.47,324.865)})
    4182.777
    """    
    summation=0
    for t in points:
        x,y=t
        summation+=y
    return summation

        

    
