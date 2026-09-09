# 문자열 내 p와 y의 개수 | Lv.1
# https://school.programmers.co.kr/learn/courses/30/lessons/12916


def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')


if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution('pPoooyY')
    print("결과:", result)
    print("기대값:", True)
