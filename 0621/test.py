def hello():
    print("Hello")

#입력받은 숫자가 짝수인가 홀수인가 확인하는 함수
def holjjak(num):
    result = ""
    if num % 2 == 0:
        result = "짝수"
    elif num % 2 == 1:
        result = "홀수"
    else:
        result = "입력받은 숫자가 정수가 아닙니다"
    return result
