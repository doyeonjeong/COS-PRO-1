# 1회 - 문제 9

"""
두 학생 A와 B는 계단 게임을 하였습니다.
계단 게임의 규칙은 아래와 같습니다.

~~~
1. 계단 제일 아래에서 게임을 시작합니다. (0번째 칸)
2. 가위바위보를 합니다.
3. 이기면 계단 세 칸을 올라가고, 지면 한 칸을 내려가고, 비기면 제자리에 있습니다.
4. 계단 제일 아래에서 지면 제자리에 있습니다.
5. 2~4 과정을 열 번 반복합니다.
~~~

A와 B가 계단 게임을 완료한 후에, A가 계단 위 몇 번째 칸에 있는지 파악하려고 합니다.

A와 B가 낸 가위바위보 기록이 순서대로 들어있는 리스트 recordA와 recordB가 매개변수로 주어질 때, 게임을 마친 후의 A의 위치를 return 하도록 solution 함수를 작성했습니다. 그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

---

#####매개변수 설명
A와 B가 낸 가위바위보 기록이 순서대로 들어있는 리스트 recordA와 recordB가 매개변수로 주어집니다.
* recordA와 recordB의 원소는 0, 1, 2중 하나이고 순서대로 가위, 바위, 보를 의미합니다.
* recordA와 recordB의 길이는 10입니다.

---

#####return 값 설명
solution 함수는 계단 게임을 마친 후에 A가 계단 위 몇 번째 칸에 위치하는지를 return 합니다.
* 계단 제일 아래 칸은 0번째 칸입니다.

---

#####예시

| recordA              | recordB              | return |
|-----------------------|-----------------------|--------|
| [2,0,0,0,0,0,1,1,0,0] | [0,0,0,0,2,2,0,2,2,2] | 14     |

#####예시 설명

||||||||||||
|----------|------|------|------|------|------|------|------|------|------|------|
| recordA | 보   | 가위 | 가위 | 가위 | 가위 | 가위 | 바위 | 바위 | 가위 | 가위 |
| recordB | 가위 | 가위 | 가위 | 가위 | 보   | 보   | 가위 | 보   | 보   | 보   |
| result   | 0    | 0    | 0    | 0    | +3   | +6   | +9   | +8   | +11  | +14  |
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def func(record):
    if record == 0:
        return 1
    elif record == 1:
        return 2
    return 0


def solution(recordA, recordB):
    cnt = 0
    for i in range(len(recordA)):
        if recordA[i] == recordB[i]:
            continue
        elif recordA[i] == func(recordB[i]):
            cnt = cnt + 3
        else:
            if cnt != 0:  # recordA의 현재 위치가 0일 때는 -1로 내려가지 않음
                cnt = cnt - 1
    return cnt


recordA = [2, 0, 0, 0, 0, 0, 1, 1, 0, 0]
recordB = [0, 0, 0, 0, 2, 2, 0, 2, 2, 2]
ret = solution(recordA, recordB)


print("solution 함수의 반환 값은", ret, "입니다.")
