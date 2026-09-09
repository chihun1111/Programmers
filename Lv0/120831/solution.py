# 짝수의 합 | Lv.0
# https://school.programmers.co.kr/learn/courses/30/lessons/120831


def solution(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)


if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution(10)
    print("결과:", result)
    print("기대값:", 30)
