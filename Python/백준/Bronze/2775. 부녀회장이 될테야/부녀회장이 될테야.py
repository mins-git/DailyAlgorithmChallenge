tc = int(input())

# num +1 만큼의 인원이 거주중.
for test in range(tc):
    floor = int(input())
    num = int(input())
    # 0층인원 뽑아보기.
    f0 = [x for x in range(1, num+1)]
    
    # 층수만큼 반복
    for k in range(floor):
        for i in range(1, num):
            f0[i] += f0[i-1]
    print(f0[-1])
