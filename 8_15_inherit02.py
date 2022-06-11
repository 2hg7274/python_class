# 예외 클래스 만들기
"""
상속은 기존에 있는 클래스를 기반으로 조금 수정해서 내가 원하는 클래스를 만들 때 사용한다.
그럼 Exception이라는 기존에 있는 클래스를 조금 수정해서 CustomException이라는 클래스를 만들어 보자.
"""

# 사용자 정의 예외 클래스 만들기
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)

raise CustomException
"""
Exception 클래스를 상속했으므로, Exception 클래스와 이름만 다르지 모두 같은 클래스이다. 
따라서 raise로 예외를 발생시키는 것도 가능하다.
"""