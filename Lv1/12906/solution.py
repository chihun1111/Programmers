# 같은 숫자는 싫어 | Lv.1
# https://school.programmers.co.kr/learn/courses/30/lessons/12906


def solution(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] == 0 or arr[i] != arr[i - 1]:
            result.append(arr[i])
    return result


if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution([1, 1, 3, 3, 0, 1, 1])
    print("결과:", result)
    print("기대값:", [1, 3, 0, 1])
