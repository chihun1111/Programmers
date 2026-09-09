# 짝수 홀수 개수 | Lv.0
# https://school.programmers.co.kr/learn/courses/30/lessons/120824


def solution(num_list):
    num = []
    x = 0
    y = 0
    for i in num_list:
        if i % 2:
            y += 1
        else:
            x += 1
    num.append(x)
    num.append(y)
    return num


if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution([1, 2, 3, 4, 5])
    print("결과:", result)
    print("기대값:", [2, 3])
