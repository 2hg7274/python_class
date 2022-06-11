# 프라이빗 변수
"""
일단 변수를 마음대로 사용하는 것을 막아야 한다.
파이썬은 클래스 내부의 변수를 외부에서 사용하는 것을 막고 싶을 때 인스턴스 변수 이름을 __<변수이름> 형태로 선언한다. 
이때 _(언더 바)기호가 두 개라는 것을 주의.
"""
# 프라이빗 변수
# 모듈을 가져온다.
import math

# 클래스를 선언.
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

# 원의 둘레와 넓이를 구한다.
circle = Circle(10)
print("#원의 둘레와 넓이를 구한다.")
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_area())
print()

# __radius에 접근
print("# __radius에 접근.")
print(circle.__radius)

"""
클래스 내부에서 __radius를 사용하는 것은 아무 문제 없지만, 클래스 외부에서 __radius를 사용하려고 할 때 그런 속성이 없다는 오류를 출력.

이처럼 속성을 선언할 때 __를 붙이기만 하면 외부에서 사용할 수 없는 변수가 된다. 
"""