# 3회 - 문제 6. 소수의 합으로 표현하기

"""
어떤 수를 서로 다른 소수 3개의 합으로 표현하는 방법의 수를 구하려 합니다.
예를 들어 33은 총 4가지 방법으로 표현할 수 있습니다.

1. 3+7+23
2. 3+11+19
3. 3+13+17
4. 5+11+17

자연수 n이 매개변수로 주어질 때, n을 서로 다른 소수 3개의 합으로 표현하는 방법의 수를 return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.
※ 1,000 이하인 소수는 168개 있습니다.

---
#####매개변수 설명

n이 solution 함수의 매개변수로 주어집니다.
* n은 1,000 이하인 자연수입니다.

---
#####return 값 설명

n을 서로 다른 소수 3개의 합으로 표현하는 방법의 수를 return 해주세요.
* 만약, n을 서로 다른 소수 3개의 합으로 표현할 수 없다면 0을 return  해주세요.

---
#####예시

| n | return |
|---|--------|
| 33 | 4 |
| 9 | 0 |

#####예시 설명

예시 #1
문제에 나온 예와 같습니다.

예시 #2
9는 서로 다른 세 소수의 합으로 나타낼 수 없습니다.
"""


def solution(n):
    answer = 0
    primes = [2]
    for i in range(3, n + 1, 2):  # 3부터 모든 홀수
        is_prime = True
        for j in range(2, i):
            if i % j == 0:  # 나누어 떨어지는 값이 있다면 False
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    primes_len = len(primes)
    for i in range(0, primes_len - 2):
        for j in range(i + 1, primes_len - 1):
            for k in range(j + 1, primes_len):
                if primes[i] + primes[j] + primes[k] == n:
                    answer += 1
    return answer


n1 = 33
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
# 결과 : solution 함수의 반환 값은 4 입니다.

n2 = 9
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
# 결과 : solution 함수의 반환 값은 0 입니다.
