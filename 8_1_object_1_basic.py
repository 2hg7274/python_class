# 학생 리스트를 선언
students = [
    {"name": "힝", "korean":60, "math":20, "science": 50},
    {"name": "비", "korean":30, "math":80, "science": 40},
    {"name": "스장", "korean":90, "math":90, "science":90}
]


# 학생을 한 명씩쓰기 반복.
print("이름", "총점", "평균", sep="\t")

for student in students:

    # 점수의 총합과 평균을 구하자.
    score_sum = student["korean"] + student["math"] + student["science"]
    score_average = score_sum / 3

    # 출력
    print(student["name"], score_sum, score_average, sep="\t")