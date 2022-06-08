# 딕셔너리를 리턴하는 함수를 선언
def create_student(name, korean, math, science):
    return {
        "name": name,
        "korean":korean,
        "math":math,
        "science":science
    }

# 학생 리스트를 선언
students = [
    create_student("힝", 60, 20, 50),
    create_student("비", 30, 80, 40),
    create_student("스장", 90, 90, 90)
]

# 학생을 한 명씩 반복
print("이름", "총점", "평균", sep='\t')
for student in students:
    # 점수의 총합과 평균을 구하자.
    score_num = student["korean"] + student["math"] + student["science"]
    score_avg = score_num/3

    # 출력
    print(student["name"], score_num, score_avg, sep='\t')