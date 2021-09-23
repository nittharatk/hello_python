'''
if __name__ == '__main__':
    N = int(input())

    my_list = []
    #eval('my_list.insert(0,5)')
    #eval('print(my_list)')
    for A in range (N):
        Commands = input()
        j = Commands.split()
        if j[0]=='print':
            print (my_list)
        elif j[0]=='insert':
            my_list.insert(int(j[1]),(j[2]))
        elif j[0]=='remove':
            x = int(j[1])
            my_list.remove(x)
        print (my_list)
            
        command = j[0]
        #print (command)
        if command == 'print':
            print (my_list)
        else:
            args = ','.join(j[1:])
            print (args)
            task = 'my_list.{0}.({1})'.format(command,args)
            #eval(task)
            #print (task)
        '''
            
        #print (task) # -> insert,0,5
        #if task[0]=='insert':
         #   my_list.insert(int(task[1]), (task[2]))
          #  print (my_list)
            
    
#eval() = String -> Command

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):    
        raw = input().split(' ')
        command = raw[0]
        if (command == 'print'):
            print(l)
        else:
            args = ','.join(raw[1:])
            task = 'l.{0}({1})'.format(command,args)
            eval(task) #string -> command**S