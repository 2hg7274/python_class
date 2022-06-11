# 데코레이터를 사용한 게와 세
"""
계와 세터를 함수로 만드는 일이 많아져서 파이썬 프로그래밍 언어는 게터와 세터를 쉽게 만들고 사용할 수 있게 기능을 제공한다.
다음과 같이 변수 이름과 같은 함수를 정의하고 위에 @property와 @<변수이름>.setter라는 데코레이터를 붙인다.
"""

# 데코레이터를 사용해 게터와 세터 만들기
# 모듈을 가져온다.
import math

# 클래스 선언
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # 게터와 세터를 선언
    @property
    def radius(self):
        return self.__radius

    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 한다.")
        else:
            self.__radius = value

# 원의 둘레와 넓이를 구한다.
print("# 데코레이터를 사용한 Getter와 Setter")
circle = Circle(10)
print("원래 원의 반지름: ", circle.radius)
circle.radius = 2
print("변경된 원의 반지름: ", circle.radius)
print()

# 강제로 예외를 발생
print("# 강제로 예외를 발생")
circle.radius = -10

"""
이렇게 하면 circle.radius를 사용하는 것만으로 자동으로 게터와 세터가 호출되도록 할 수 있다.
지금까지 계속 언급했던 것처럼 기존의 사용 방법과 같은 방법으로 객체를 사용할 수 있는 것이다. 
"""