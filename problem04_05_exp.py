#! /usr/bin/python3

'''
Problem 4
세자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마?
(모르겠어서 구글 참고함)
'''

number_list = []

for i in range(400, 1000):
    for j in range(400, 1000):
        
        number = str(i*j)

        if number[0] == number[5] and number[1] == number[4] and number[2] == number[3]:
            number_list.append(int(number))

print('4번:',max(number_list))

''' NOTE: 파이썬 컴파일러가 어떤 원리로 작성된지는 모르겠지만... 
위의 소스에서만 제가 생각하는 수정되었으면 하는 부분이 있는데요.

l = []
num_list = list(range(999, 400, -1)) # 반복하는 부분은 변수로 빼는게 가독성과 성능면에서 더 낫습니다.
for i in num_list:
    for j in num_list:
        n = str(i*j) # l 과 함께, 이런 변수명은 이런 작은 부분에서만 괜찮겠죠. 또는 작은 함수내
        if n[0] == n[5] and n[1] == n[4] and n[2] == n[3]:
            l.append(n) # 이 부분은 큰 차이가 안날 수도 있지만, 첨언하자면, 
                        # 굳이 int 형으로 변형 할 필요까지는 없을 수도 있습니다.
                        # 물론, string 보다는 int를 access하는 게 성능면에서는 더 좋겠지만

print(max(l))


'''



'''
Problem 5
1~20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
(모르겠음)
'''

num = 1
num_list = [2,3,5,7,11,13,17,19]

for k in num_list:
    
    while True:
        if k*k > 20:
            num *= k
            break
        k *= k

print('5번:', num)













