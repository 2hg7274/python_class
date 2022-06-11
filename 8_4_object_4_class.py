# 클래스 선언
class Student:
    def __init__(self, name, korean, math, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.science

    def get_avg(self):
        return self.get_sum()/3

    def to_string(self):
        return "{}\t{}\t{}" .format(self.name, self.get_sum(), self.get_avg())

# 학생 리스트 선언
students = [
    Student("힝", 60, 20, 50),
    Student("비", 30, 80, 40),
    Student("스장", 90, 90, 90)
] 

# 학생을 한 명씩 반복
print("이름", "총점", "평균", sep='\t')
for i in students:
    # 출력
    print(i.to_string())
