#! /usr/bin/python3
'''
8번. 다음은 연속된 1000자리 수입니다 (읽기 좋게 50자리씩 잘라 놓음).

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

여기서 붉게 표시된 71112의 경우 연속한 5개 숫자 7, 1, 1, 1, 2를 모두 곱하면 14입니다. 또, 그 다음 연속한 5개 숫자 11121의 경우 1, 1, 1, 2, 1을 모두 곱하면 2입니다.

이런 식으로 맨 처음 (7 × 3 × 1 × 6 × 7 = 882) 부터 맨 끝 (6 × 3 × 4 × 5 × 0 = 0) 까지 연속한 5개 숫자의 곱을 구할 수 있습니다.

이렇게 구할 수 있는 연속한 5개 숫자의 곱 중에서 가장 큰 값은 얼마입니까?

'''
    
num = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

def times(list):

    mul = 1

    for i in list:
        mul *= i

    return mul

def get_five(number):

    mnum = 0

    for j in range(len(number)-4):
        fnum = number[j:j+5]

        num_list = [int(k) for k in fnum]

        multipled = times(num_list)
        
        if mnum < multipled:
       
            mnum = multipled  
    print(mnum)

get_five(num)


# 구글링해서 줄인 코드
def get_five2(n):
    
    m_list = []
    for i in range(len(n)-4):
        m_list.append(int(n[i]) * int(n[i+1]) * int(n[i+2]) * int(n[i+3]) * int(n[i+4]))
    
    print(max(m_list))

get_five2(num)

'''
9번.
세 자연수 a, b, c 가 피타고라스 정리 a^2 + b^2 = c^2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
예를 들면 32 + 42 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.

a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?
'''
def prob8():

    for a in range(1,1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if (a * a) + (b * b) == (c * c) and a < b < c:
                print(a * b * c)

prob8()