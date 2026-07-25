from collections import Counter
import math

def solution(str1, str2):
    
    answer = 0
    # str1 = clean(str1)
    # str2 = clean(str2)
    arr1 = []
    arr2 = []
    
    # 두 글자씩 어떻게 쪼갤까
    for i in range(len(str1)-1):
        pair = str1[i:i+2]
        if pair.isalpha():
            arr1.append(pair.lower())
        
    for i in range(len(str2)-1):
        pair = str2[i:i+2]
        if pair.isalpha():
            arr2.append(pair.lower())
    
    c1 = Counter(arr1)
    c2 = Counter(arr2)
    
    inter = sum((c1 & c2).values())
    union = sum((c1 | c2).values())
    
    # 둘 다 공집합이라면 
    if union == 0:
        return 65536
    
    answer = (inter / union) * 65536
    
    return math.floor(answer)

# def clean(str):
    
#     arr = []
    
#     for s in str:
#         if s.isalpha():
#             arr.append(s.lower())
#         elif s.isdecimal():
#             arr.append(s)
    
#     string = ''.join(arr)
    
#     return string
      