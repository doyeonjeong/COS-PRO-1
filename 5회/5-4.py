# 5회 - 문제 4.

"""
주어진 숫자를 각 숫자와 숫자의 개수로 읽으려 합니다. 이때, 값이 큰 숫자를 먼저 읽어야합니다.
예를 들어, 2433은 2 한개 4 한개 3 두개로 이루어져 있기 때문에 "413221"로 읽습니다. 
숫자 number가 매개변수로 주어질 때, 숫자를 읽어 문자열로 return 하도록 solution 함수를 작성했습니다. 그러나, 일부 코드가 잘못되어 코드가 바르게 동작하지 않습니다. 주어진 코드가 모든 입력을 바르게 처리하도록 코드를 수정해주세요. 코드는 _**한 줄**_만 수정해야 합니다.

---

#####매개변수 설명
숫자 number가 solution 함수의 매개변수로 주어집니다.
* number는 0 이상 2,000,000,000 이하인 정수입니다.

---
#####return 값 설명
주어진 숫자를 읽어 문자열 형태로 return 합니다.

---
#####예시

| number | return |
|--------|----------|
| 2433 | "413221" |
| 662244 | "624222" |

#####예시 설명
예시 #1
문제에 나온 예와 같습니다.

예시 #2
662244는 6 두개 2 두개 4 두개로 이루어져 있기 때문에 "624222"로 읽습니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(number):
    answer = ''
    number_count = [0 for _ in range(10)]
    while number > 0:
        number_count[number % 10] += 1
        number //= 10
    for i in range(10):
        if number_count[i] != 0:
            answer = (str(i) + str(number_count[i])) + answer
    return answer


number1 = 2433
ret1 = solution(number1)

print("solution 함수의 반환 값은", ret1, "입니다.")
# 결과 : solution 함수의 반환 값은 413221 입니다.

number2 = 662244
ret2 = solution(number2)

print("solution 함수의 반환 값은", ret2, "입니다.")
# 결과 : solution 함수의 반환 값은 624222 입니다.
