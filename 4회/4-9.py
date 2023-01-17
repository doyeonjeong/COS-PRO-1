# 4회 - 문제 9. 분침과 시침의 각도 구하기

"""
hour 시 minute 분에 아날로그 시계의 시침과 분침이 몇 도를 이루는지 계산하려 합니다. 예를 들어, 3시 00분에 시침과 분침은 90˚를 이룹니다.
어떤 시점의 시 hour, 분 minute이 매개변수로 주어질 때, hour 시 minute 분에 아날로그 시계의 시침과 분침이 이루는 각도를 소숫점 첫번째 자리까지 표현한 문자열을 return 하도록 solution 함수를 작성해주세요.

---
#####매개변수 설명

어떤 시점의 시 hour, 분 minute이 solution 함수의 매개변수로 주어집니다.

* hour는 1 이상 12 이하인 자연수입니다.
* minute은 0 이상 59 이하인 정수입니다.

---

#####return 값 설명

hour 시 minute 분에 아날로그 시계의 시침과 분침이 이루는 각도를 소숫점 첫번째 자리까지 표현한 문자열을 return 하세요.
* 단, 각도는 __소수점 이하 첫째 자리까지__ 표현하세요.

---
#####예시

| hour | minute | return |
|---|---|---|
| 3 | 0 | "90.0" |

#####예시 설명

앞서 설명한 예와 같습니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(hour, minute):
    h = (360/12) * hour + (360/12/16) * minute  # 시침
    m = (360/60) * minute  # 분침
    # print(h, m, abs(h-m), m-h, 360 - abs(h-m))
    answer = abs(h-m)
    if answer > 180:
        answer = 360 - answer
    return "{:.1f}".format(answer)


hour = 3
minute = 0
ret = solution(hour, minute)

print("solution 함수의 반환 값은", ret, "입니다.")
# 결과 : solution 함수의 반환 값은 90.0 입니다.
