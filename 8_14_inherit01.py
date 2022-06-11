# 상속
"""
클래스 기반의 객체 지향 언어들은 상속이라는 기능을 지원한다. 

## 상속
컴퓨터를 조립해 본 적이 있나?
메인보드라는 것은 어디에 좋은 것인지, 메모리는 어느 회사 제품이 좋은지 등을 전혀 모르는데, 
그래서 '다나와'라는 사이트에서 '표준 컴퓨터'라고 되어 있는 적당한 가격대의 컴퓨터를 고른 뒤에 'CPU는 제일 비싼 것으로 사야겠지'라며 CPU만 교체한다.

이처럼 다른 누군가가 만들어 놓은 기본 형태에 내가 원하는 것만 교체하는 것이 바로 '상속'이다.

## 다중 상속
건담 프라모델을 조립해 본 적이 있나? 
필자의 경우는 같은 회사에서 시리즈로 나오는 건담 프라모델을 한 번에 구입하는 편이다.
이렇게 구입하면 규격이 모두 같기 때문에 멋있는 몸, 멋있는 얼굴, 멋있는 팔, 멋있는 다리, 멋있는 무기만 뽑아 새로운 건담을 만들 수 있다.

이처럼 다른 누군가가 만들어 놓은 형태들을 조립해서 내가 원하는 것을 만드는 것도 '상속'이다.
이를 다중상속이라 부른다.


프로그래밍 언어는 기반이 되는 것을 부모라고 부르고, 이를 기반으로 생성한 것을 자식이라고 부른다. 
부모가 자식에게 자신의 기반을 물려주는 기능이므로 '상속'이라고 부르는 것이다. 
"""

# 상속의 활용
# 부모 클래스를 선언.
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init__() 메소드가 호출되었다.")
    
    def test(self):
        print("Parent 클래스의 test() 메소드이다.")

# 자식 클래스를 선언.
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init__() 메소드가 호출되었다.")

# 자식 클래스의 인스턴스를 생성하고 부모의 메소드를 호출
child = Child()
child.test()
print(child.value)

"""
Child 클래스 내부에는 아무것도 없는데, Parent 클래스의 상속을 받았으므로 Parent 클래스가 가지고 있는 함수와 변수를 활용할 수 있는 것이다.
"""