T = int(input())
dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for t in range(1, T + 1):
    N, hexa = input().split()
    N = int(N)

    num = int(hexa, 16)
    num = (bin(num) [2:])

    print(f"#{t} {num.rjust(N * 4, '0')}")