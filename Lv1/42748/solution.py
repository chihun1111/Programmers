# K번째수 | Lv.1
# https://school.programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
	result = []
	for command in commands:
		result.append(
			sorted(array[command[0] - 1:command[1]])[command[2] - 1])
	return result


if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    print("결과:", result)
    print("기대값:", [5, 6, 3])
