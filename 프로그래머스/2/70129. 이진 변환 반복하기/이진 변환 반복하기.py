def solution(s):
    answer = []
    count = 0
    i = 0

    while s != "1":
        count += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        i += 1

    answer = [i, count]

    return answer