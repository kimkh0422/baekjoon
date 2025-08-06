count = int(input("지금까지 본 과목 개수를 입력하세요: "))
gradeDict = {}
totalGrade = 0

for i in range(count):
    subject = input("과목을 입력하세요: ")
    grade = int(input("점수를 입력하세요: "))
    gradeDict[subject] = grade
    totalGrade += grade
    
avgGrade = totalGrade/count
print(gradeDict)
print(f"평균 점수: {avgGrade}")
    