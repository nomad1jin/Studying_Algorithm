arr = ["{", "}", "(", ")"]
T = int(input())

for t in range(1, T+1):
    string = input()
    stack = []
    result = 1

    for s in string:
        if s == "{" or s == "(":
            stack.append(s)
        elif s == "}":
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                result = 0
                break
        elif s == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                result = 0
                break


    if stack:
        result = 0
    
    print(f"#{t} {result}")

