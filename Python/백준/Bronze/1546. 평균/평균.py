import statistics

tc = int(input())
score_list = list(map(int, input().split()))

M = max(score_list) #최대값

newscore = []

# /M*100 의 값으로 리스트 생성.
for testcase in score_list :
    v = testcase / M * 100
    newscore.append(v)

# 리스트의 평균 구하기.
avg = statistics.mean(newscore)
print(avg)