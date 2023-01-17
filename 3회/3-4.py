# 3회 - 문제 4. 중복 문자열 이어붙이기

"""
두 문자열 s1과 s2를 붙여서 새 문자열을 만들려 합니다. 이때, 한 문자열의 끝과 다른 문자열의 시작이 겹친다면, 겹치는 부분은 한 번만 적습니다.
예를 들어 s1 = "ababc", s2 = "abcdab"일 때, 아래와 같이 s1 뒤에 s2를 붙이면 새 문자열의 길이는 9입니다.
![string2.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/b4bd8f93a2/61f4238b-bcc7-435c-a203-da6ebb27d968.png)
그러나 s2 뒤에 s1을 붙이면 새 문자열의 길이는 8로, 더 짧게 만들 수 있습니다.
![string3.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/e983c2cd38/9ffb7a01-73f3-47d5-aa39-b97543cf7973.png)
두 문자열 s1과 s2가 매개변수로 주어질 때, s1과 s2를 붙여서 만들 수 있는 문자열 중, 가장 짧은 문자열의 길이를 return 하도록 solution 함수를 완성해주세요.

##### 제한 조건
두 문자열 s1과 s2가 solution 함수의 매개변수로 주어집니다.

* s1과 s2의 길이는 1 이상 100 이하입니다.
* s1과 s2는 알파벳 소문자로만 이루어져 있습니다.

##### 입출력 예

| s1      | s2       | return |
|---------|----------|--------|
| "ababc" | "abcdab" | 8      |

##### 입출력 예 설명

문제에 주어진 예시와 같습니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math


def solution(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    # s1 - s2비교
    for i in range(is_smaller(s1_len, s2_len), s1_len):
        if s1[i:] == s2[0:s1_len-i]:
            break
    result1 = s1_len - i
    # s2 - s1비교
    for i in range(is_smaller(s2_len, s1_len), s2_len):
        if s2[i:] == s1[0:s2_len-i]:
            break
    result2 = s2_len - i
    return s1_len + s2_len - max(result1, result2)

# 비교 대상이 더 작다면


def is_smaller(s1_len, s2_len):
    return s2_len - s1_len if s2_len < s1_len else 0


s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")
# 결과 : solution 함수의 반환 값은 8 입니다.

s3 = "ababc"
s4 = "efghi"
ret = solution(s3, s4)

print("solution 함수의 반환 값은", ret, "입니다.")
# 결과 : solution 함수의 반환 값은 9 입니다.

'''
[1]
s1[0:]  a b a b c
s2[0:5] a b c d a b
-> 겹치는 문자 없음

[2]
s1[1:]  a b a b c
s2[0:4]   a b c d a b
-> 겹치는 문자 없음

[3]
s1[2:]  a b a b c
s2[0:3]     a b c d a b
-> 겹치는 문자 : abc -> break

[4]
s1[3:]  a b a b c
s2[0:2]       a b c d a b
-> 겹치는 문자 없음

[5]
s1[2:]  a b a b c
s2[0:1]         a b c d a b
-> 겹치는 문자 없음

[6] 겹치는 문자가 없는 경우 break가 발생하지 않는다.
✨ s1의['여기':]값의 범위 : i = 0 ~ 4
✨ s2의[:'여기']값의 범위 : j = 5 ~ 1 ❓ s1_len - i // 앞에있는 문자열의 길이

[7] 문자열의 길이가 더 짧은것을 기준으로 반대쪽도 맞춰본다.
s2[1:] a b c d a b
s1[0:5]  a b a b c
-> 겹치는 문자 없음

[8]
s2[2:] a b c d a b
s1[0:4]    a b a b c
-> 겹치는 문자 없음

[9]
s2[3:] a b c d a b
s1[0:3]      a b a b c
-> 겹치는 문자 없음

[10]
s2[4:] a b c d a b
s1[0:2]        a b a b c
-> 겹치는 문자 : ab -> break

[11]
s2[5:] a b c d a b
s1[0:1]          a b a b c
-> 겹치는 문자 

[12] 
✨ s2의['여기':]값의 범위 : i = 1 ~ 5
✨ s1의[:'여기']값의 범위 : j = 5 ~ 1 ❓ s2_len - i // 앞에있는 문자열의 길이

'''
