# 5회 - 문제 6.

"""
p 진법으로 표현한 수란, 각 자리를 0부터 p-1의 숫자로만 나타낸 수를 의미합니다. p 진법으로 표현한 자연수 두개를 더한 결과를 q 진법으로 표현하려 합니다.
예를 들어, 3진법 수 112001과 12010을 더한 결과를 8진법으로 나타내면 1005입니다.
solution 함수의 매개변수로 p 진법 자연수를 담은 문자열 s1, s2와 두 수를 나타내는 진법의 기수 p, 두 수의 덧셈 결과를 표현할 진법의 기수 q가 매개변수로 주어집니다. p진법으로 표현된 두 수를 더한 결과를 q 진법으로 나타낸 값을 return 하도록 solution 함수를 완성해주세요.

---
#####매개변수 설명

p 진법으로 자연수를 담은 문자열 s1, s2와 두 수를 표현한 진법의 기수 p, 두 수의 덧셈 결과를 표현할 진법의 기수 q가 solution 함수의 매개변수로 주어집니다.
* p와 q는 2 이상 10 이하인 자연수입니다.
* s1과 s2의 길이는 1 이상 9 이하입니다.
* s1과 s2의 원소는 '0', '1', '2', …, ‘p-1’로만 구성됩니다.
* s1이나 s2가 ‘0’인 경우는 주어지지 않습니다.

---
#####return 값 설명

두 수를 더한 결과를 q 진법으로 나타낸 값을 문자열로 return 하도록 solution 함수를 완성해주세요.

---
#####예시

| s1 | s2 | p | q | return |
|-----|-----|---|---|---------|
| "112001" | "12010" | 3 | 8 | "1005" |

#####예시 설명

문제에 나온 예와 같습니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import string

tmp = string.digits+string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(s1, s2, p, q):
    p_sum = int(s1, p) + int(s2, p)
    return convert(p_sum, q)


s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

print("solution 함수의 반환 값은", ret, "입니다.")
# 결과 : solution 함수의 반환 값은 1005 입니다.
