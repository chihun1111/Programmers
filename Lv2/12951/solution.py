# JadenCase 문자열 만들기 | Lv.2
# https://school.programmers.co.kr/learn/courses/30/lessons/12951


def solution(s):
    result = []
    is_first = True

    for char in s:
        if char == ' ':
            result.append(' ')
            is_first = True
        else:
            if is_first:
                result.append(char.upper())
                is_first = False
            else:
                result.append(char.lower())
    return "".join(result)

if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution("3people   unFollowed me")
    print("결과:", result)
    print("기대값:", "3people   Unfollowed Me")
