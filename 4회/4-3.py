# 4회 - 문제 3. 스키장 최소 비용 구하기

"""
정확히 n 일 연속으로 스키장 이용하는데 필요한 최소 비용을 계산하려 합니다. 다음은 스키장에서 판매하는 이용권입니다.

| 이용권 종류 | 스키장을 사용할 수 있는 일수                   | 가격          |
|-------------|---------------------------------------|---------------|
| one_day     | 구매한 날 하루 동안 사용 가능         | one_day_price |
| multi_day   | 구매한 날부터 multi_day일간 사용 가능 | multi_day_price     |

예를 들어 one_day_price = 3, multi_day = 5, multi_day_price = 14라면, 1일 이용권은 3원, 5일 이용권은 14원입니다. n = 6일 때 정확히 6일 연속으로 스키장을 이용하는데 필요한 비용은 다음과 같이 계산합니다.

* 1일 이용권 x 6장 → 6 x 3원 = 18원
* 1일 이용권 x 1장 + 5일 이용권 x 1 장 → 1 x 3원 + 1 x 14원 = 17원

따라서 정확히 6일 연속 스키장을 이용하려면 최소 17원이 듭니다.
※ 스키장을 정확히 6일간 이용해야 하므로 5일 이용권을 두 장 살 수는 없습니다.

solution 함수의 매개변수로 one_day_price, multi_day, multi_day_price, n가 주어집니다. 이때 정확히 n일 연속 스키장을 이용하는데 필요한 최소 금액을 계산해서 return 하도록 solution 함수를 작성했습니다. 그러나, 일부 코드가 잘못되어 코드가 바르게 동작하지 않습니다. 주어진 코드가 모든 입력을 바르게 처리하도록 코드를 수정해주세요. 코드는 _**한 줄**_만 수정해야 합니다.

---

#####매개변수 설명

one_day_price, multi_day, multi_day_price, n이 순서대로 solution 함수의 매개변수로 주어집니다.

* one_day_price는 1일 이용권의 가격을 나타냅니다.
* one_day_price는 1 이상 1000 이하인 자연수입니다.
* multi_day_price는 multi_day일 이용권의 가격을 나타냅니다.
* multi_day_price는 1 이상 1000 이하인 자연수입니다.
* multi_day는 3 이상 5 이하인 자연수입니다.
* n은 1 이상 10^12 이하인 자연수입니다.

---

#####return값 설명

정확히 n일 연속으로 스키장을 이용하는데 필요한 최소 금액을 return 해주세요.

---
#####예시

| one_day_price | multi_day | multi_day_price  | n  | result |
|---|---|----|----|--------|
| 3 | 5 | 14 | 6  | 17     |
| 2 | 3 | 5  | 11 | 19     |

#####예시 설명
예시 #1
앞서 설명한 예와 같습니다.

예시 #2
1일 이용권은 2원, 3일 이용권은 5원입니다. 정확히 11일 동안 스키장을 이용할 때 드는 최소 비용은 다음과 같습니다.

* 1일 이용권 x 2장 + 3일 이용권 x 3 장 → 2 x 2원 + 3 x 5원 = 19원
"""


def solution(one_day_price, multi_day, multi_day_price, n):
    if one_day_price * multi_day <= multi_day_price:
        return n * one_day_price
    else:
        return (n // multi_day) * multi_day_price + (n % multi_day) * one_day_price


one_day_price1 = 3
multi_day1 = 5
multi_day_price1 = 14
n1 = 6
ret1 = solution(one_day_price1, multi_day1, multi_day_price1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
# 결과 : solution 함수의 반환 값은 17 입니다.

one_day_price2 = 2
multi_day2 = 3
multi_day_price2 = 5
n2 = 11
ret2 = solution(one_day_price2, multi_day2, multi_day_price2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
# 결과 : solution 함수의 반환 값은 19 입니다.
