T = int(input())
arr = []
clap = ['3', '6', '9']

for i in range(1, T + 1):
    string = str(i)

    if len(string) < 2:
        if string not in clap:
            arr.append(string)
        else:
            arr.append("-")

    else:
        tmp = ""

        for j in string:
            if j in clap:
                tmp += "-"

        if tmp == "":
            arr.append(string)
        else:
            arr.append(tmp)

print(" ".join(arr))
