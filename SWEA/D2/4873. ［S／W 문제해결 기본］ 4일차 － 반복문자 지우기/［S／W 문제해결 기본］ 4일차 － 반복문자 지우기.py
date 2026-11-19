T = int(input())

for t in range(1, T + 1):
    str = input()
    stack = []
    
    for s in str:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
            
    print(f"#{t} {len(stack)}")
            