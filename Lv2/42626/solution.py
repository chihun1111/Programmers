# 더 맵게 | Lv.2
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1

        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)

        new_scoville = min1 + min2 * 2

        heapq.heappush(scoville, new_scoville)

        count += 1

    return count


if __name__ == "__main__":
    # 테스트 케이스 1: 기본 예제 (기대값: 2)
    print("테스트 1:", solution([1, 2, 3, 9, 10, 12], 7))

    # 테스트 케이스 2: 이미 모든 스코빌 지수가 K 이상인 경우 (기대값: 0)
    print("테스트 2:", solution([7, 8, 9, 10], 7))

    # 테스트 케이스 3: 모든 음식을 섞어도 K 이상으로 만들 수 없는 경우 (기대값: -1)
    print("테스트 3:", solution([1, 1, 1], 100))

    # 테스트 케이스 4: 원소가 2개뿐이고 한 번만 섞으면 되는 경우 (기대값: 1)
    print("테스트 4:", solution([1, 5], 7))

    # 테스트 케이스 5: 원소가 2개인데 섞어도 K를 넘지 못하는 경우 (기대값: -1)
    print("테스트 5:", solution([1, 2], 10))

    # 테스트 케이스 6: 0이 포함된 경우 (기대값: 2)
    print("테스트 6:", solution([0, 2, 3], 5))

    # 테스트 케이스 7: 숫자가 큰 경우의 테스트 (기대값: 4)
    print("테스트 7:", solution([10, 11, 12, 2], 30))