### 학생 객체와 관련된 부분
# 딕셔너리를 리턴하는 함수를 선언.
def create_student(name, korean, math, science):
    return {
        "name":name,
        "korean":korean,
        "math":math,
        "science":science
    }
# 학생을 처리하는 함수를 선언.
def student_get_sum(student):
    return student["korean"]+student["math"]+student["science"]

def student_get_avg(student):
    return student_get_sum(student) / 3

def student_to_string(student):
    return "{}\t{}\t{}" .format(
        student["name"],
        student_get_sum(student),
        student_get_avg(student)
        
    )



### 객체를 활용하는 처리
# 학생 리스트를 선언
students = [
    create_student("힝", 60, 20, 50),
    create_student("비", 30, 80, 40),
    create_student("스장", 90, 90, 90)
]

# 학생을 한 명씩 반복
print("이름", "총점", "평균", sep='\t')
for student in students:
    # 출력
    print(student_to_string(student))



Class CodeStates:
    클래스 내용

인스턴스 이름(변수이름) = 클래스 이름() -> 생성자 함수라고 부름.

# 클래스를 선언
class Student:
    pass

# 학생을 선언
student = Student()

# 학생 리스트를 선언.
students = [
    Student(),
    Student(),
    Student()
]


#생성자
클래스 이름과 같은 함수를 생성자라고 부른다. 
클래스 내부에 __init__라는 함수를 만들면 객체를 생성할 때 처리할 내용을 작성할 수 있다. 
"""
class 클래스 이름:
    def __init__(self, 추가적인 매개변수):
        pass
"""
self는 '자기자신'을 나타내는 딕셔너리라고 생각하면 된다.
다만 self가 가지고 있는 속성과 기능에 접근할 때는 self.<식별자>형태로 접근.

# 클래스로 나타내어보자
# 클래스를 선언
class Student:
    def __init__(self, name, korean, math, science):
        self.name = name,
        self.korean = korean,
        self.math = math,
        self.science = science

# 학생 리스트를 선언.
students = [
    Student("힝", 60, 20, 50),
    Student("비", 30, 80, 40),
    Student("스장", 90, 90, 90)
] 

# Student인스턴스의 속성에 접근하는 방법
student[0].name -> "힝"
student[0].korean -> 60

    
# 메소드
클래스가 가지고 있는 함수를 메소드라고 부른다. 
"""
class 클래스 이름:
    def 메소드 이름(self, 추가적인 매개변수):
        pass
"""
