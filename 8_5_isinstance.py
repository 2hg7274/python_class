# 어떤 클래스의 인스턴스인지 확인하기
"""
일단 객체(인스턴스)가 어떤 클래스로부터 만들어졌는지 확인할 수 있도록  ininstance() 함수를 제공한다.
insinstance() 함수는 첫 번째 매개변수에 객체(인스턴스), 두 번째 매개변수에 클래스를 입력한다. 
    -> isinstance(인스턴스, 클래스)

이때 인스턴스가 해당 클래스를 기반으로 만들어졌다면 True, 전혀 상관이 없는 인스턴스와 클래스라면 False를 리턴한다.

***단순한 인스턴스 확인***
단순한 인스턴스 확인이라면 다음과 같은 방법도 사용할 수 있다. 
    -> type(student) == Student
다만 이 방법은 '상속을 사용할 때' 다르게 동작한다. 

isinstance()함수는 다양하게 활용할 수 있는 기능이다. 
간단한 예로 하나의 리스트 내부에 여러 종류의 인스턴스가 들어 있을 때, 인스턴스들을 구분하며 속성과 기능을 사용할 때 사용한다.
"""

# isinstance() 함수 활용 
# 학생 클래스를 선언.
class Studnet:
    def study(self):
        print("공부를 합니다.")

# 선생님 클래스를 선언.
class Teacher:
    def teach(self):
        print("학생을 가르친다.")

# 교실 내부의 객체 리스트를 생성.
classroom = [Studnet(), Studnet(), Teacher(), Studnet(), Studnet()]

# 반복을 적용해서 적절한 함수를 호출.
for person in classroom:
    if isinstance(person, Studnet):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

"""
일반적으로 객체 지향 프로그래밍은 모든 데이터를 클래스로 구현한다. 
이러한 데이터를 관리할 때 리스트를 따로 만들고 활용해야 한다고 생각하는 경우가 많은데, isinstance()함수를 사용하면 
이처럼 여러 종류의 데이터를 다룰 수 있다. 
"""