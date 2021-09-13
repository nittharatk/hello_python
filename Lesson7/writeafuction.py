def is_leap(year):
    leap = False
    
    # Write your logic here
    
    '''
    year = 1990
    year % 4 == 0 #true
    year % 100 == 0 #false
    year % 400 == 0 #true
    
    2020 = True
    2004 = True
    2003 = False
    2100 = False
    2021 = False
    2008 = True
    1900 = False
    100000 = True
    '''

   
    if (year % 4 == 0):
        leap = True
        if (year % 100 == 0): 
            if (year % 400 == 0): 
                leap = True
            else : 
                leap = False
        else :
            leap = True
            
    else :
        leap = False
    
    
    return leap

year = int(input())
print(is_leap(year))

"""
def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 == 0):
        leap = True
        if (year % 100 == 0):
            leap = False
            if (year % 400 == 0):
                leap = True
  
    return leap
"""