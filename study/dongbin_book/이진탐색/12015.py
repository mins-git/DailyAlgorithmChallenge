import sys
import bisect
sys.stdin = open('input.txt')


"수열 A가 주어졌을때 가장 긴 증가하는 부분 수열을 구하는 프로그램작성"
"가장 긴 증가 부분 수열?"


def length_of_lis(sequence):
    lis = [] # 개수체크할 리스트 선언

    for num in sequence: # sequence다 체크하기.
        pos = bisect.bisect_left(lis, num) # lis에서 num이 들어갈 위치를 체크

        if pos == len(lis): # pos와 lis의 길이가 같으면 마지막에 숫자 넣으면됨.
            lis.append(num) # pos는 인덱스 요소이기 때문
        else:
            lis[pos] = num # num이 들어갈 위치에 lis를 넣어주기.

    return len(lis) # 길이 출력해주면 가장 긴 증가하는 부분 수열 길이 나옴

N = input()
sequence = list(map(int, input().split()))

print(length_of_lis(sequence))