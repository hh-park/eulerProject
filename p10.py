#! /usr/bin/python3

'''
10번. 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

이백만(2,000,000) 이하 소수의 합은 얼마입니까?

'''
# 소수 구하는 알고리즘이 이해가 계속 안됨..구글링..

def prob10(n):
    
    l = []
    total = 0
    for i in range(2,n):
        chk = True
        for j in range(2,i):
            if i % j == 0:
                chk = False
                break
        if chk:
            l.append(i)
        
    # print(l)
    
    print(sum(l))

'''
11번. pass
'''
