n = int(input())
result = []
score_num = []
last_num = []
for x in range (n):
    name = input()
    score = float(input())
    score_num.append(score)
    result.append([name,score])
    score_num.sort()
    score_num.reverse()
    num_count = score_num.count(min(score_num))
    main_number = score_num[len(score_num)-num_count-1]
    for i in range (n):
        if main_number == result[i][1]:
            last_num.append(result[i][0])
            last_num.sort()
            for j in range(len(last_num)):
                print(last_num[j])
