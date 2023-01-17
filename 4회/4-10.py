# 4회 - 문제 10. 소수의 세제곱이 몇개가 있나요

"""
자연수를 제곱한 수는 제곱수, 세 제곱한 수는 세제곱 수라고 합니다. 예를 들어 2^2 = 4 는 제곱수, 3^3 = 27은 세제곱수 입니다.
두 자연수 a, b가 주어질 때 a 이상 b 이하인 자연수 중 _**소수**_의 제곱수와 세제곱수의 개수를 구하려 합니다. 예를 들어 a = 6, b = 30일 때 소수의 제곱수는 [9, 25]로 2개, 소수의 세제곱수는 [8, 27]로 2개로 총 4개입니다.
두 자연수 a, b가 매개변수로 주어질 때, a 이상 b 이하인 제곱수와 세제곱수의 개수의 합을 return 하도록 solution 함수를 완성해주세요.

---
#####매개변수 설명

두 자연수 a, b가 solution 함수의 매개변수로 주어집니다.

* a, b는 각각 1 이상 1,000,000,000 이하인 자연수입니다.
* a ≤ b인 경우만 입력으로 주어집니다.

---
#####return 값 설명
 a 이상 b 이하인 제곱수와 세제곱수의 개수의 합을 return 해주세요.

---
#####예시

| a | b  | return |
|---|----|--------|
| 6 | 30 | 4 |

#####예시 설명
6 이상 30 이하인 수중 소수의 제곱수는 다음과 같습니다.

* 3^2 = 9
* 5^2 = 25

소수의 세제곱 수는 다음과 같습니다.

* 2^3 = 8
* 3^3 = 27

따라서 4를 return 하면 됩니다.
"""
import math


def get_prime(b):           # b = 30
    e = int(math.sqrt(b))   # e = 5
    is_prime = [0] * (e+1)  # is_prime[x] = 0 -> prime number, 1 -> False
    prime = []
    for i in range(2, e+1):
        if is_prime[i] == 0:
            prime.append(i)  # i는 소수 목록에 추가
            for x in range(i+i, e+1, i):
                is_prime[x] = 1
    return prime


def solution(a, b):
    answer = 0
    prime = get_prime(b)
    for p in prime:
        t1, t2 = p**2, p**3
        if a <= t1 <= b:
            answer += 1
        if a <= t2 <= b:
            answer += 1
    return answer

# print(get_prime(30)) # 2, 3, 5


a = 6
b = 30
ret = solution(a, b)

print("solution 함수의 반환 값은", ret, "입니다.")
# 결과 : solution 함수의 반환 값은 4 입니다.
