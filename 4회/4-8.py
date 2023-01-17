# 5회 - 문제 8. n번째로 작은 수 구하기

"""
1 이상 9 이하 숫자가 적힌 카드를 이어 붙여 숫자를 만들었습니다. 이때, 숫자 카드를 조합해 만든 수 중에서 n이 몇 번째로 작은 수인지 구하려 합니다.
예를 들어, 숫자 카드 1, 2, 1, 3로 만들 수 있는 수를 작은 순으로 나열하면 [1123, 1132, 1213, 1231, 1312, ... , 3121, 3211]입니다. n이 1312라면, 숫자 카드를 조합해 만든 수 중 n은 n은 5번째로 작은 수입니다.
숫자 카드를 담은 리스트 card, 수 n이 매개변수로 주어질 때 숫자 카드를 조합해 만든 수 중에서 n이 몇 번째로 작은 수인지 return 하도록 solution 함수를 완성해주세요.

---

#####매개변수 설명

카드에 적힌 숫자를 담은 리스트 card, 수 n이 solution 함수의 매개변수로 주어집니다.

* card는 길이가 9 이하인 리스트입니다.
* card의 원소는 1 이상 9 이하인 자연수입니다.
* n은 999,999,999 이하인 자연수입니다.
* n의 자릿수는 리스트 card의 길이와 같습니다.
* n의 각 자리의 숫자는 1 이상 9 이하입니다.

---

#####return 값 설명

숫자 카드를 조합해 만든 수 중에서 n이 몇 번째로 작은 수인지 return 해주세요.
* 만약, n을 만들 수 없다면 -1을 return 해주세요.

---
#####예시

| card | n | return |
|----|----|----|
| [1, 2, 1, 3] | 1312 | 5 |
| [1, 1, 1, 2] | 1122 | -1 |

#####예시 설명

예시 #1
앞서 설명한 예와 같습니다.

예시 #2
숫자 카드를 조합하면 [1112, 1121, 1211, 2111]를 만들 수 있습니다. 따라서 1122는 만들 수 없습니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

num_list = []


def solution(card, n):
    card_cnt = get_card_cnt(card)
    num_list.clear()  # or global num_list -> global num_list를 비우겠다.
    card_pick(0, len(card), card_cnt, [0]*10, 0)
    # print(num_list)
    return num_list.index(n) + 1 if n in num_list else -1


def get_card_cnt(card):
    card_cnt = [0] * 10
    for x in card:
        card_cnt[x] += 1
    return card_cnt

# level: 몇번째 카드를 뽑는 것 인가? 0 -> 1 -> 2 -> 3 -> 4
# max_level: 총 뽑을 카드의 수 : len(card)
# card_cnt: 각 번호 카드가 몇 장 있는지 표기한 것
# card_used: number를 만들기 위해 각 번호 카드가 몇 장 사용되었는지 표기한 것
# number: 만들어지고 있는/만들어진 숫자


def card_pick(level, max_level, card_cnt, card_used, number):
    if level == max_level:
        num_list.append(number)
        return

    for i in range(1, 10):
        if card_cnt[i] > card_used[i]:
            card_used[i] += 1
            card_pick(level + 1, max_level, card_cnt,
                      card_used, number * 10 + i)
            card_used[i] -= 1


card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
# 결과 : solution 함수의 반환 값은 5 입니다.

card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
# 결과 : solution 함수의 반환 값은 -1 입니다.
