# 4회 - 문제 4. 마방진

"""
마방진이란 가로, 세로, 대각선 방향의 수를 더한 값이 모두 같은 정사각형 행렬입니다. 마방진에는 `1`부터 `정사각형 넓이`까지, 수가 하나씩 배치되어야 합니다. 아래는 가로, 세로, 대각선 방향의 수를 더한 값이 모두 34인 4 x 4 마방진입니다.
  ![KakaoTalk_Photo_2018-09-15-17-58-10.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/762ea16c04/303fdbe0-89ed-4f74-87b9-1ed047cf2c7c.png)
4 x 4 행렬의 두 빈칸을 채워 행렬을 마방진으로 완성하려 합니다. 빈칸은 0으로 표시합니다. 이를 위해 다음과 같이 프로그램 구조를 작성했습니다.

```
1. 두 빈칸의 위치를 찾습니다.
2. 숫자 1 ~ 16 중 존재하지 않는 숫자 2개를 찾습니다.
3. 첫 번째 빈칸에 작은 숫자를, 두 번째 빈칸에 큰 숫자를 넣어 행렬이 마방진이 되는지 검사합니다.
  4-1. 마방진이라면 [작은 숫자의 행 번호, 작은 숫자의 열 번호, 작은 숫자, 큰 숫자의 행 번호, 큰 숫자의 열 번호, 큰 숫자]를 return 합니다.
  4-2. 마방진이 아니라면 [큰 숫자의 행 번호, 큰 숫자의 열 번호, 큰 숫자, 작은 숫자의 행 번호, 작은 숫자의 열 번호, 작은 숫자]를 return 합니다.
```

4 x 4 크기 2차원 리스트 matrix가 매개변수로 주어질 때, 이때 빈칸의 위치와 각 칸에 들어갈 수를 담은 리스트를 return 하도록 solution 함수를 작성하려 합니다. 위 구조를 참고하여 코드가 올바르게 동작하도록 빈칸에 주어진 func_a, func_b, func_c 함수와 매개변수를 알맞게 채워주세요.

* 주어진 행렬은 빈칸을 채우면 반드시 마방진으로 완성할 수 있습니다.

---

#####매개변수 설명

2차원 리스트 matrix가 solution 함수의 매개변수로 주어집니다.

* matrix는 크기가 4 x 4인 2차원 리스트입니다.
* matrix에는 0이 반드시 두 개 들었습니다.
* matrix에는 1 이상 16 이하인 자연수 14개가 겹치지 않게 들었습니다.

---
#####return 값 설명

빈칸의 위치와 각 칸에 들어갈 수를 담은 리스트를 return 해주세요.

---
#####예시

| matrix | return |
|--------|--------|
| [[16,2,3,13],[5,11,10,0],[9,7,6,12],[0,14,15,1]] | [4,1,4,2,4,8] |

#####예시 설명

예시 #1

  ![KakaoTalk_Photo_2018-09-15-18-01-27.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/3228b4e06c/bc8300f8-1e7b-4c77-88a7-82f64f6a53bc.png)

위 그림에서 빈칸은 (4, 1)과 (2, 4)입니다. 각 칸에 4와 8을 채우면 마방진이 완성됩니다. 따라서 [작은 숫자의 행 번호, 작은 숫자의 열 번호, 작은 숫자, 큰 숫자의 행 번호, 큰 숫자의 열 번호, 큰 숫자]를 return 해야 합니다. 답은 [4, 1, 4, 2, 4, 8]입니다.

  ![KakaoTalk_Photo_2018-09-15-18-01-27 (1).png](https://grepp-programmers.s3.amazonaws.com/files/ybm/07b49bd9cc/06b0e5b9-27ba-49e7-9782-089ca97cd15b.png)

"""


def func_():
    return 0

# matrix에 존재하지 않는 두 개의 숫자 찾기


def func_a(matrix):
    n = 4
    ret = []
    exist = [False for _ in range(n * n + 1)]

    for i in range(0, n):
        for j in range(0, n):
            exist[matrix[i][j]] = True
    for i in range(1, n * n + 1):
        if exist[i] == False:
            ret.append(i)
    return ret

# matrix에서 빈칸 2개를 찾아 [[행, 열], [행, 열]] 정보를 반환


def func_b(matrix):
    n = 4
    ret = []
    for i in range(0, n):
        for j in range(0, n):
            if matrix[i][j] == 0:
                ret.append([i, j])
    return ret

# 마방진인지 확인하기


def func_c(matrix):
    n = 4
    goal_sum = sum(range(1, n * n + 1)) // n
    for i in range(0, n):
        row_sum = 0
        col_sum = 0
        for j in range(0, n):
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]
        if row_sum != goal_sum or col_sum != goal_sum:
            return False

    main_diagonal_sum = 0
    skew_diagonal_sum = 0
    for i in range(0, n):
        main_diagonal_sum += matrix[i][i]  # 우측 대각선
        skew_diagonal_sum += matrix[i][n - 1 - i]  # 좌측 대각선
    if main_diagonal_sum != goal_sum or skew_diagonal_sum != goal_sum:
        return False
    return True


def solution(matrix):
    answer = []
    coords = func_b(matrix)
    nums = func_a(matrix)

    matrix[coords[0][0]][coords[0][1]] = nums[0]
    matrix[coords[1][0]][coords[1][1]] = nums[1]

    if func_c(matrix):
        for i in range(0, 2):
            answer.append(coords[i][0] + 1)
            answer.append(coords[i][1] + 1)
            answer.append(nums[i])
    else:
        matrix[coords[0][0]][coords[0][1]] = nums[1]
        matrix[coords[1][0]][coords[1][1]] = nums[0]
        for i in range(0, 2):
            answer.append(coords[1-i][0] + 1)
            answer.append(coords[1-i][1] + 1)
            answer.append(nums[i])
    return answer


matrix = [[16, 2, 3, 13], [5, 11, 10, 0], [9, 7, 6, 12], [0, 14, 15, 1]]
ret = solution(matrix)

print("solution 함수의 반환 값은", ret, "입니다.")
# 결과 : solution 함수의 반환 값은 [4, 1, 4, 2, 4, 8] 입니다.
