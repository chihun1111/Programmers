# 약수의 합 | Lv.1
# https://school.programmers.co.kr/learn/courses/30/lessons/12928


def solution(n):
	if n == 1:
		return 1
	result = 1 + n
	i = 2
	while i * i <= n:
		if n % i == 0:
			result += i
			if i != n // i:
				result += n // i
		i += 1
	return result



if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution(12)
    print("결과:", result)
    print("기대값:", 28)
