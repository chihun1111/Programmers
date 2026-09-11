# 최댓값과 최솟값 | Lv.2
# https://school.programmers.co.kr/learn/courses/30/lessons/12939


def solution(s):
    num = s.split(" ")
    maxn = int(num[0])
    minn = maxn
    for i in num:
        maxn = max(maxn, int(i))
        minn = min(minn, int(i))
    result = [str(minn), str(maxn)]
    return " ".join(result)

# def solution(s):
#   # 1. 공백으로 쪼개고, 모든 요소를 한 번에 정수(int)로 변환
#   nums = list(map(int, s.split()))

#   # 2. 내장 min, max 함수를 쓰고 f-string으로 바로 합치기
#   return f"{min(nums)} {max(nums)}"

if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution("1 2 3 4")
    print("결과:", result)
    print("기대값:", "1 4")
