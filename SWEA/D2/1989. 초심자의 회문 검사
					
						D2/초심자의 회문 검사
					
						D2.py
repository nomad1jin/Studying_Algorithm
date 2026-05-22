T = int(input())
for tc in range(1, T+1):
    s = input()
    stack = []
    answer = True
    
    for i in range(0, len(s) // 2):
        stack.append(s[i])
            
    if len(s) % 2 == 0:
        start = len(s) // 2
    else :
        start = len(s) // 2 + 1
     
    for i in range(start, len(s)):
        if stack.pop() != s[i]:
            answer = False
            break

    print(f"#{tc} {1 if answer else 0}")