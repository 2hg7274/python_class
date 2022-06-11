# 특수한 이름의 메소드
"""
우리가 만든 Student 클래스를 기반으로 객체를 만들고 객체 뒤에 .(마침표)를 입력해서 자동 완성 기능을 살펴보면 
우리가 만들지 않았던 함수들이 잔뜩 들어 있는 것을 확인할 수 있다. 

이는 모두 파이썬이 클래스를 사용할 때 제공해 주는 보조 기능이다. 
그런데 이름들이 조금 특이하다. 
__<이름>__() 형태로 되어 있다. 이러한 메소드는 특수한 상황에 자동으로 호출되도록 만들어졌다.

우선 다음과 같이 __str__()을 클래스 내부에 정의해 보자. 
이렇게 __str__() 함수를 정의하면 str() 함수를 호출할 때 __str__() 함수가 자동으로 호출된다. 
"""

# __str__() 함수
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
        return self.get_sum() / 3

    # __str__() 이름으로 함수를 선언
    def __str__(self):
        return "{}\t{}\t{}" .format(
            self.name, self.get_sum(), self.get_avg()
        )

# 학생 리스트를 선언.
students = [
    Student("힝", 60, 20, 50),
    Student("비", 30, 80, 40),
    Student("스장", 90, 90, 90)
]

# 출력
print("이름", "총점", "평균", sep='\t')
for student in students:
    print(str(student)) #str() 함수의 매개변수로 넣으면 __str__()함수가 호출.