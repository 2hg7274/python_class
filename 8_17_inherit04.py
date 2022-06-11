"""
추가로 기존에 있던 함수/변수 이외의 것을 완전히 새로 정의하는 것도 가능하다
"""
# 자식 클래스로써 부모에 없는 새로운 함수 정의하기
# 사용자 정의 예외를 생성.
class CustomException(Exception):
    def __init__(self, messgae, value):
        Exception.__init__(self)
        self.message = messgae
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("#### 오류 정보 ####")
        print("메시지: ", self.message)
        print("값: ", self.value)

# 예외를 발생시켜 보자
try:
    raise CustomException("딱히 이유 없음", 273)
except CustomException as e:
    e.print()

