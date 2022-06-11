# 게터와 세터
"""
그런데 중간에 원의 둘레를 변경하고 싶다면 어떻게 해야할까?
클래스 외부에서 직접 __radius 속성에 접근할 수 없기 때문에 간접적으로 접근할 수 있는 방법을 찾아야 한다. 

이때 사용되는 것이 게터와 세터이다. 
게터와 세터는 프라이빗 변수의 값을 추출하거나 변경할 목적으로, 간접적으로 속성에 접근하도록 해주는 함수이다.
"""
# 게터와 세터
# 모듈을 가져온다.
import math

# 클래스 선언.
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    
    # 게터와 세터를 선언.
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value

# 원의 둘레와 넓이를 구한다.
circle = Circle(10)
print("# 원의 둘레와 넓이를 구한다.")
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_area())
print()


# 간접적으로 __radius에 접근
print("# __radius에 접근")
print(circle.get_radius())
print()

# 원의 둘레와 넓이를 구한다.
circle.set_radius(2)
print("# 반지름을 변경하고 원의 둘레와 넓이를 구한다.")
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_area())

"""
get_radius()함수와 set_radius()함수를 만들어서 함수로 프라이빗 변수의 갑에 접근하거나, 값을 변경하게 했다.

이렇게 함수를 사용해 값을 변경하면 여러 가지 처리를 추가할 수 있다. 
예를 들어 set_radius()함수에 다음과 같은 코드를 추가하면 __radius에 할당할 값을 양의 숫자로만 한정할 수 있다.

## 게터와 세터로 변수를 안전하게 사용하기
def set_radius(self, value):
    if value <= 0:
        rais TypeError("길이는 양의 숫자여야 한다.")
    self.__radius = value
"""