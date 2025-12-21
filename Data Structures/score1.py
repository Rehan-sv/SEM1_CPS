ans=input("Enter the  answer key: ")
n=int(input("Enter the number of students: "))

marks=[]
scores=[]
for i in range(n):
    options=input(f"Enter the ansers{i+1}").split()
score=0
for j in len(ans):
    if ans[j]==options[j]:
        score+=1
    scores.append(scores)
    marks.append[j]
        
        