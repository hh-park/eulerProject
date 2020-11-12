#! /usr/bin/python3

'''
Problem 6
1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다 (제곱의 합).
12 + 22 + ... + 102 = 385
1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
(1 + 2 + ... + 10)2 = 552 = 3025
따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의 차이는 3025 - 385 = 2640 이 됩니다.
그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마입니까?
'''

def prob6():

    l = list(range(1,101))
    sum = 0 # 합
    sum_s = 0 # 제곱의 합
    square = 0 # 합의 제곱

    for i in l:

        sum_s += i * i        # NOTE: 이런 모양인 경우, 언어에 따라서 오동작 할 수 있으므로, 다음과 같이 명확하게 구분해 주어야 합니다.
                              # sum_s += (i*i), 오동작의 원인은 += 연산 기호가 * 보다 앞설 수도 있기 때문
        sum += i
        sqaure = sum * sum    # NOTE: 이 부분은 for 문 바깥이어야 하지 않아요?

    print(sqaure - sum_s)

prob6()

'''
Problem 7
소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
이 때 10,001번째의 소수를 구하세요.
(진짜 모르겠어서 구글 많이 참고함...)
'''


# 소수 / 약수 확인        ## NOTE: 직접 짠 소스가 이 부분인거죠?
def is_prime(num):

    if num == 1:
        return False # 1은 소수가 아니므로 False 반환

    i = 2

    while i < num:
        if num % i == 0: # 나누어 떨어지는 수가 있으면
            return False # 바로 False를 리턴하고 함수를 종료함
  
        i += 1
    return True

# 테스트 과정
number = 82385683       # NOTE: 이건 뭔가요?
i = 1

while i <= number:
    if number % i == 0 and is_prime(i):
        print(i, "is prime factor")
    i += 1

# 남의 답

def isPrime(n):
    number = 2
    prime_numbers = [2]
    l = []

    while len(prime_numbers) < n:
        number = number + 1
        for i in prime_numbers:
            l.append(number % i)
            if number % i == 0:
                break

        if 0 in l:    
            l = []
            continue
        else:
            prime_numbers.append(number)
    print(prime_numbers[n-1])


isPrime(10001)




