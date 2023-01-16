# 3회 - 문제 3. 비숍으로부터 도망쳐

"""
체스에서 비숍(Bishop)은 아래 그림과 같이 대각선 방향으로 몇 칸이든 한 번에 이동할 수 있습니다. 만약, 한 번에 이동 가능한 칸에 체스 말이 놓여있다면 그 체스 말을 잡을 수 있습니다.
![bishop1.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/07fd25eb65/561e9310-6ee3-4ecf-85bd-dd573bdbb8df.png)
8 x 8 크기의 체스판 위에 여러 개의 비숍(Bishop)이 놓여있습니다. 이때, 비숍(Bishop)들에게 _**한 번에**_ 잡히지 않도록 새로운 말을 놓을 수 있는 빈칸의 개수를 구하려고 합니다.
위 그림에서 원이 그려진 칸은 비숍에게 한 번에 잡히는 칸들이며, 따라서 체스 말을 놓을 수 있는 빈칸 개수는 50개입니다.
8 x 8 체스판에 놓인 비숍의 위치 bishops가 매개변수로 주어질 때, 비숍에게 한 번에 잡히지 않도록 새로운 체스 말을 놓을 수 있는 빈칸 개수를 return 하도록 solution 함수를 완성해주세요.

---
#####매개변수 설명
체스판에 놓인 비숍의 위치 bishops가 solution 함수의 매개변수로 주어집니다.
* bishops는 비숍의 위치가 문자열 형태로 들어있는 리스트입니다.
* bishops의 길이는 1 이상 64 이하입니다.
* 비숍이 놓인 위치는 알파벳 대문자와 숫자로 표기합니다.
  * 알파벳 대문자는 가로 방향, 숫자는 세로 방향 좌표를 나타냅니다.
  * 예를 들어 위 그림에서 비숍이 있는 칸은 "D5"라고 표현합니다.
* 한 칸에 여러 비숍이 놓이거나, 잘못된 위치가 주어지는 경우는 없습니다.

---
#####return 값 설명
비숍에게 한 번에 잡히지 않도록 새로운 체스 말을 놓을 수 있는 빈칸의 개수를 return 해주세요.

---
#####예시

| bishops            | return |
|--------------------|--------|
| ["D5"]             | 50     |
| ["D5", "E8", "G2"] | 42     |

#####예시 설명
예시 #1
문제에 나온 예시와 같습니다.

예시 #2
  ![bishop2.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/b635b0d993/71863e6c-1320-4ce1-8b5b-886c37dcfa5b.png)

그림과 같이 원이 그려진 칸은 비숍에게 한 번에 잡히는 칸들이며, 따라서 체스 말을 놓을 수 있는 빈칸 개수는 42개입니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math


def solution(bishops):
    answer = 0
    matrix = [[0] * 9 for _ in range(9)]  # 0,0 ~ 8,8 -> 0번째 줄 사용 안함
    dyx = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

    for bishop in bishops:
        y = int(bishop[1])       # 세로
        x = ord(bishop[0]) - ord('A') + 1  # 가로

        matrix[y][x] = 1
        for dy, dx in dyx:
            ny, nx = y, x
            while True:
                ny += dy
                nx += dx
                if not in_validate(ny, nx):
                    break
                matrix[ny][nx] = 1
    for y in range(1, 9):
        for x in range(1, 9):
            if matrix[y][x] == 0:
                answer += 1
    return answer


def in_validate(y, x):
    if 1 <= y <= 8 and 1 <= x <= 8:
        return True
    return False


bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")
# 결과 : solution 함수의 반환 값은 50 입니다.

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")
# 결과 : solution 함수의 반환 값은 42 입니다.

'''
[체스판 만들기] [1, 1] ~ [8, 8]
matrix = []
for i in range(8):
    matrix.append([])
    for j in range(8):
        matrix[i].append((i+1, j+1))

print(matrix)
[[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)],
 [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)],
 [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)],
 [(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)],
 [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)],
 [(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)],
 [(7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)],
 [(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]]
'''
