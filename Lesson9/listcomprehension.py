if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    i = list(range(0,x+1))
    #print (i)
    
    j = list(range(0,y+1))
    #print (j)
    
    k = list(range(0,z+1))
    #print (k)
    
    '''
    output = []
    for i in range (0, x+1):
        for j in range (0, y+1):
            for k in range (0, z+1):
                if i+j+k != n:
                    output.append([i,j,k])
    print (output)           
    '''
    
    #List comprehension
    print([[i,j,k] for i in range (0, x+1) for j in range (0, y+1) for k in range (0, z+1) if i+j+k != n])