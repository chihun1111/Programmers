# 배열의 평균값 | Lv.0
# https://school.programmers.co.kr/learn/courses/30/lessons/120817


def solution(numbers):
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("결과:", result)
    print("기대값:", 5.5)
