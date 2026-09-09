# 특정 문자 제거하기 | Lv.0
# https://school.programmers.co.kr/learn/courses/30/lessons/120826


def solution(my_string, letter):
    return ''.join(i for i in my_string if i != letter)


if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution('abcdef', 'f')
    print("결과:", result)
    print("기대값:", 'abcde')
