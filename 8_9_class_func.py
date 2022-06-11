# 클래스 함수
"""
클래스 함수도 클래스 변수처럼 그냥 클래스가 가진 함수이다. 
일반적인 함수로 만드나 클래스 함수로 만드나 사용에는 큰 차이가 없다. 
다만 '클래스가 가진 기능'이라고 명시적으로 나타내는 것 뿐이다. 

그런데 생성하는 방법이 조금 특이하다.
@classmethod 부분을 데코레이터라고 부른다. 

## 클래스 함수 만들기
class 클래스 이름:
    @classmethod
    def 클래스 함수(cls, 매개변수):
        pass 

클래스 함수의 첫 번째 매개변수에는 클래스 자체가 들어온다. 
일반적으로 cls(그냥 '클래스'라고 읽으면 된다.)라는 이름의 변수로 선언하며, 이렇게 만들어진 클래스 함수는 다음과 같이 사용한다.

## 클래스 함수 호출하기
클래스 이름.함수 이름(매개변수)
"""
# 클래스 함수
# 클래스 선언.
class Student:
    # 클래스 변수
    count = 0
    studnets = []

    # 클래스 함수
    @classmethod
    def print(cls):
        print("----- 학생목록 -----")
        print("이름\t총점\t평균")
        for student in cls.studnets: #student.students라고 해도 상관없지만, 여기서는 매개변수로 받은 cls를 활용
            print(str(student))
        print("----- ----- -----")

    
    # 인스턴스 함수
    def __init__(self, name, korean, math, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.science = science
        Student.count += 1
        Student.studnets.append(self)

    
    def get_sum(self):
        return self.korean + self.math + self.science

    def get_avg(self):
        return self.get_sum() / 3

    def __str__(self):
        return "{}\t{}\t{}" .format(
            self.name, self.get_sum(), self.get_avg()
        )

# 학생 리스트 선언.
Student("힝", 60, 20, 50),
Student("비", 30, 80, 40),
Student("스장", 90, 90, 90)


# 현재 생성된 학생을 모두 출력
Student.print()