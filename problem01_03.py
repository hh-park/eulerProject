#! /usr/bin/python3

'''
Problem 1
1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면?
'''
sum1 = 0

for i in range(1000):
    
    if i % 3 == 0 or i % 5 == 0:
        sum1 += i

print('1번:', sum1)


'''
Problem 2
피보나치 수열에서 400만 이하이면서 짝수인 항의 합 
'''
arr = [1,2]
sum2 = 0

for j in range(30):

    sum2 = arr[j] + arr[j+1]
    arr.append(sum2)

sum3 = 0

for index in range(len(arr)):
    
    if arr[index] % 2 == 0 and arr[index] <= 4000000:
        
        sum3 += arr[index]

print('2번:',sum3)

# 다른 사람 풀이
'''
i1 = 0
i2 = 1
i3 = i1 + i2
total = 0

while i3<4000000:
    
    i3 = i1+i2
    i1 = i2
    i2 = i3
    if i3 % 2 == 0:
        total += i3

print(total)
'''

'''
Problem 3
가장 큰 소인수 구하기
(몰라서 검색함)
'''
list3 = []
a = 600851475143
b = 2

while a != 1:
    if a % b == 0:
        a /= b
        list3.append(b)
    else:
        b += 1

print('3번:',max(list3))













