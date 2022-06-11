# 클래스 변수와 메소드
"""
인스턴스가 속성과 기능을 가질 수도 있지만, 클래스가 속성(변수)과 기능(함수)을 가질 수도 있다.

## 클래스 변수
클래스 변수를 만드는 방법부터 살펴보자.
클래스 변수는 class 구문 바로 아래의 단계에 변수를 선언하기만 하면 된다.

### 클래스 변수 만들기
class 클래스 이름:
    클래스 변수 = 값

### 클래스 변수에 접근하기
클래스 이름.변수 이름

그냥 클래스가 가지고 있는 변수이므로, 사용 방법은 일반 변수와 다르지 않다.
"""

# 클래스 변수
# 클래스 선언.
class Student:
    count = 0

    def __init__(self, name, korean, math, science):
        #인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.science = science

        # 클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었다." .format(Student.count))

# 학생 리스트 선언.
students = [
    Student("힝", 60, 20, 50),
    Student("비", 30, 80, 40),
    Student("스장", 90, 90, 90)
]

# 출력
print()
print("현재 생성된 총 학생 수는 {}명입니다." .format(Student.count))

"""
사실 일반적인 변수로 만드나 클래스 변수로 만드나 사용에는 큰 차이가 없다. 
하지만 '클래스가 가진 기능'을 명시적으로 나타내서 변수를 만든다는 것이 포인트.
"""