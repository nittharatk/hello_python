if __name__ == '__main__':
    students = []
    grade = []
    ans = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        grade.append(score)

    A = sorted(set(grade))
    for i in range(len(students)):
        if students[i][1] == A[1]:
            #print (students[i][0])
            name_A = students[i][0]
            ans.append(name_A)
    
    ans = sorted(ans)
    for i in range(len(ans)):
        print (ans[i])
    #print (A)