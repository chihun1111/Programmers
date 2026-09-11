# 올바른 괄호 | Lv.2
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
	stack = []
	for char in s:
		if char == '(':
			stack.append(char)
		elif char == ')':
			if stack:
				stack.pop()
			else:
				return False
	return len(stack) == 0

if __name__ == "__main__":
	# 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
	result = solution("()()))")
	print("결과:", result)
	print("기대값:", True)
