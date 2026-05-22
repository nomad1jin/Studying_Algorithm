T = int(input())
dict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

def ten_to_binary(n):
    ans = ''
    for i in range(4):        
        ans = str(n % 2) + ans
        n //= 2
    return ans

for test_case in range(1, T + 1):
	n, hex_num = input().split(" ")
	ans = ''
	for hex in hex_num:
		if hex.isnumeric():
			ans += ten_to_binary(int(hex))   
		else :
			ans += ten_to_binary(dict[hex])
     
	print(f"#{test_case} {ans}")