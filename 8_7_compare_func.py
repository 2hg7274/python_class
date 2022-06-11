"""
따라서 이전의 to_string()함수가 아니라 str(객체)라는 지금까지 사용했던 것과 같은 방법으로
객체를 문자열로 변환할 수 있다. 
특수한 이름의 함수들이 많이 있는데, 자동 완성 기능의 설명을 보면 대략적으로 어떤 기능을 가진 것인지 알 수 있다.

몇 가지 특이한 이름을 정리해 보면 다음과 같다.
다음은 크기 비교 함수 이름이다.
    eq: equal: 같다
    ne: not equal: 다르다
    gt: greater than: 크다
    ge: greater than or equal: 크거나 같다
    lt: less than: 작다
    le: less than or equal: 작거나 같다
이를 활용해 학생들을 성적으로 비교할 수 있도록 만들어 보자.
"""
# 크기 비교 함수 
# 클래스를 선언.
class Student:
    def __init__(self, name, korean, math, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.science

    def get_avg(self):
        return self.get_avg() / 3

    def __str__(self, student):
        return "{}\t{}\t{}" .format(
            self.name, self.get_sum(student), self.get_avg(student)
        )

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

# 학생 리스트 선언.
students = [
    Student("힝", 60, 20, 50),
    Student("비", 30, 80, 40),
    Student("스장", 90, 90, 90)
]

# 학생을 선언.
student_a = Student("힝", 60, 20, 50)
student_b = Student("스장", 90, 90, 90)

# 출력
print("student_a == student_b = ", student_a==student_b)
print("student_a != student_b = ", student_a!=student_b)
print("student_a > student_b = ", student_a>student_b)
print("student_a >= student_b = ", student_a>=student_b)
print("student_a < student_b = ", student_a<student_b)
print("student_a <= student_b = ", student_a<=student_b)
