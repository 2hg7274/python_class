# 프라이빗 변수와 게터/세터
"""
객체 지향 프로그래밍의 최종 목표는 객체를 효율적으로 만들고 사용하는 것이다.
객체를 효율적으로 사용하기 위한 추가 기능을 알아보기 위해 간단한 예를 살펴보자.
"""
# 원의 둘레와 넓이를 구하는 객체 지향 프로그램
# 모듈을 가져온다
import math

# 클래스를 선언
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_circumference(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * (self.radius ** 2)


# 원의 둘레와 넓이를 구하라.
circle = Circle(10)
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ",circle.get_area())

"""
만약 Circle 클래스의 radius 속성에 다음과 같이 음수를 넣으면 어떻게 될까? 
"""
# 원의 둘레와 넓이를 구하라.
circle = Circle(10)
circle.radius = -2
print()
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ",circle.get_area())

"""
원의 넓이는 제곱해서 괜찮지만, 둘레는 음수가 나온다.
현실에서는 길이가 음수가 될 수 없다.
따라서 길이를 음수로 넣는 것을 막는 방법이 필요하다. 
"""