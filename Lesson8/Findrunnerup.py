if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #print (sorted(set(arr)))
    
       
    #Score = (n, list(arr))
    #print (Score)
    
    Score = set(list(arr))
    #print (Score)
    j = sorted(Score)
    print (j[-2])