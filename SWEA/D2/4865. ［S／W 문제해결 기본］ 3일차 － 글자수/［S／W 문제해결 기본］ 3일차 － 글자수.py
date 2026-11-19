
T = int(input())

for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    string = []
    dic = {}

    for i in str1:
        if i not in string:
            string.append(i)

    for j in str2:
        if j in dic and j in string:
            dic[j] += 1
        else:
            dic[j] = 1
       
    print(f"#{t} {max(dic.values())}")     
