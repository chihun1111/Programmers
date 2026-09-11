# 기능개발 | Lv.2
# https://school.programmers.co.kr/learn/courses/30/lessons/42586


def solution(progresses, speeds):
    days = []
    for i, progress in enumerate(progresses):
        day = 0
        progress = int(progress)
        for is_progress in range(progress, 100 , speeds[i]):
            if is_progress == 100:
                break
            else:
                day += 1
        days.append(day)
    count = 0
    result = []
    max_day = days[0]
    for i in days:
        if max_day >= i:
            count += 1
        else:
            result.append(count)
            max_day = i
            count = 1
    result.append(count)
    return result

if __name__ == "__main__":
    # 공식 예제 1개를 확인합니다. 미구현 상태에서는 결과가 None입니다.
    result = solution([93, 30, 55], [1, 30, 5])
    print("결과:", result)
    print("기대값:", [2, 1])
