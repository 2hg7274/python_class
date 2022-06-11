"""
몇 가지 수정을 해보자. 
일단 __init__() 내부에서 간단한 출력을 해보게 하고 __str__() 함수를 만들어 원하는 형태로 수정하자.
"""
# 자식 클래스로써 부모의 함수 재정의(오버라이드)하기
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("#### 내가 만든 오류가 생성되었다! ####")

    def __str__(self):
        return "오류가 발생!"

raise CustomException

"""
참고로 __str__() 함수는 부모(Exception 클래스)에도 정의되어 있다.
이처럼 부모에 정의되어 있는 함수를 자식에서 다시 정의하는 것을 재정의 또는 오버라이드라고 부른다.

코드를 실행하면 출력이 약간 바뀌는 모습을 확인할 수 있다.
"""