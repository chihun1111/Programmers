# 올바른 괄호 | Lv.2
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

from collections import Counter

def solution(s):
	list(s)
	check1 = [chr(40), chr(93), chr(125)]
	check2 = [chr(41), chr(93), chr(125)]
	for i in range(len(s)):
		if s[i] in check1[0]:
			for j in range(len(s)):
				if s[j] in check2[0]:
					s[j].replace(check2[0],"")
					break
	if s in check2[0]:
		print(1)
	cut = Counter(s.split())
	if (cut[chr(34)] % 2 == 0) and (cut[chr(39)] % 2 == 0 ):
		return True
	return False


if __name__ == "__main__":
	# 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
	result = solution("()()))")
	print("결과:", result)
	print("기대값:", True)
