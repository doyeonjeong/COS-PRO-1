# 1회 - 문제 5

"""
다음과 같이 n x n 크기의 격자에 1부터 n x n까지의 수가 하나씩 있습니다.
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC1_qysbr6.png)
이때 수가 다음과 같은 순서로 배치되어있다면 이것을 n-소용돌이 수라고 부릅니다.
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC2_ol8snc.png)
소용돌이 수에서 1행 1열부터 n 행 n 열까지 대각선상에 존재하는 수들의 합을 구해야 합니다.
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC3_cbcdg3.png)
위의 예에서 대각선상에 존재하는 수의 합은 15입니다.
격자의 크기 n이 주어질 때 n-소용돌이 수의 대각선상에 존재하는 수들의 합을 return 하도록 solution 함수를 완성해주세요.

---
##### 매개변수 설명
격자의 크기 n이 solution 함수의 매개변수로 주어집니다.

* n은 1 이상 100 이하의 자연수입니다.

---
##### return 값 설명
n-소용돌이 수의 대각선상에 존재하는 수들의 합을 return 해주세요.

---
##### 예시

| n 	| return 	|
|---	|--------	|
| 3 	| 15     	|
| 2 	| 4      	|

##### 예시 설명
예시 #1
문제의 예와 같습니다.

예시 #2
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC4_astq7q.png)
1과 3을 더하여 4가 됩니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math


def solution(n):
    answer = 0
    matrix = [[0] * n for _ in range(n)]
    r = 0  # row
    c = -1  # col
    dir = 0  # 0-우, 1-하, 2-좌, 3-상 반복됨
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    loop = n  # 해당하는 방향으로 몇번 전진하는지
    num = 0  # matrix 안의 값
    while num < n * n:
        for _ in range(loop):
            r += dr[dir]
            c += dc[dir]
            num += 1
            matrix[r][c] = num
            if r == c:  # 0,0 / 1,1 / 2,2 / 3,3 이런식으로 양쪽 모두 동일한 숫자의 위치일 때 대각선임
                answer += num  # answer에 누적한다
        dir = (dir + 1) % 4  # 0, 1, 2, 3 이렇게 계속 반복해야하기 때문에
        if dir % 2 == 1:  # 1은 파이썬에서 true
            loop -= 1  # dir 홀수일 때 반복되는 수가 줄어든다
    return answer


n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
# 결과 : solution 함수의 반환 값은 15 입니다.

n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
# 결과 : solution 함수의 반환 값은 4 입니다.
