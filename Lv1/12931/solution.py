# 자릿수 더하기 | Lv.1
# https://school.programmers.co.kr/learn/courses/30/lessons/12931


def solution(n):
	result = 0
	while n > 0:
		c = n % 10
		result += c
		n = n // 10
	return result



if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution(123)
    print("결과:", result)
    print("기대값:", 6)
