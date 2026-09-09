# 짝수와 홀수 | Lv.1
# https://school.programmers.co.kr/learn/courses/30/lessons/12937


def solution(num):
    return ('Even' if num % 2 == 0 else 'Odd')


if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution(3)
    print("결과:", result)
    print("기대값:", 'Odd')
