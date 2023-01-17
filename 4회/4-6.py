# 4회 - 문제 6. 자아도취 수

"""
어떤 자리 수 k가 주어졌을 때 각 자릿수의 k 제곱의 합이 원래 수가 되는 수를 자아도취 수라고 합니다. 예를 들어 153은 세 자리 자아도취 수입니다.
![IMG](http://res.cloudinary.com/drsnvubas/image/upload/c_scale,w_400/v1518153392/narci_qsawna.png)
자연수 k가 매개변수로 주어질 때, k 자리 자아도취 수들을 리스트에 오름차순으로 담아 return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.

---

#####매개변수 설명
k가 solution 함수의 매개변수로 주어집니다.
* k는 3 이상 6 이하인 자연수입니다.

---

#####return 값 설명

k 자리 자아도취 수를 오름차순으로 정렬한 뒤 리스트에 담아 return 합니다.

---

#####예시

| k | return               |
|---|----------------------|
| 3 | [153, 370, 371, 407] |

#####예시 설명

* 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
* 370 = 3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370
* 371 = 3^3 + 7^3 + 1^1 = 27 + 343 + 1 = 371
* 407 = 4^3 + 0^3 + 7^3 = 64 + 0 + 343 = 407
"""

# exponent 제곱수를 구하는 함수
# power(2, 3) => 2 ** 3, 2^3


def power(base, exponent):
    val = 1
    for i in range(exponent):
        val *= base
    return val


def solution(k):
    answer = []
    bound = power(10, k)
    for i in range(bound // 10, bound):
        current = i
        calculated = 0
        while current != 0:
            calculated += power(current % 10, k)
            current //= 10
        if calculated == i:
            answer.append(i)
    return answer


k = 3
ret = solution(k)

print("solution 함수의 반환 값은", ret, "입니다.")
# 결과 : solution 함수의 반환 값은 [153, 370, 371, 407] 입니다.
