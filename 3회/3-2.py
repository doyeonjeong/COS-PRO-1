# 3회 - 문제 2. 팰린드롬 문제

"""
앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다. 예를 들어, "aba"는 팰린드롬이며 "abccca"는 팰린드롬이 아닙니다.

어떤 문자열의 부분 문자열 중 팰린드롬인 문자열이 여럿일 수 있습니다.
이 중 k번째로 큰 팰린드롬을 알고 싶습니다. k번째로 큰 팰린드롬이란, 모든 팰린드롬을 __사전 순__으로 나열했을 때 k번째에 위치하는 팰린드롬을 뜻합니다. 이를 위해 다음과 같이 프로그램 구조를 세웠습니다.

```
1. 팰린드롬 문자열을 저장할 리스트 palindromes를 선언합니다.
2. 주어진 문자열의 모든 부분 문자열을 찾아 다음을 수행합니다.
 2-1. 부분 문자열이 팰린드롬 문자열인지 확인하고, 팰린드롬 문자열이라면 palindromes에 같은 문자열이 이미 들어있는지 확인합니다.
 2-2. palindromes에 같은 문자열이 없으면, 현재 팰린드롬 문자열을 추가합니다.
3. palindromes를 정렬합니다.
4. 리스트 길이가 k보다 작다면 "NULL"을 리턴합니다.
5. 그렇지 않으면 리스트의 k-1번째 원소를 리턴합니다.
```

문자열 s와 숫자 k가 매개변수로 주어질 때, k번째로 큰 팰린드롬 문자열을 return 하도록 solution 함수를 작성하려 합니다. 위 구조를 참고하여 코드가 올바르게 동작하도록 빈칸에 주어진 func_a, func_b, func_c 함수와 매개변수를 알맞게 채워주세요.

---
#####매개변수 설명

문자열 s와 숫자 k가 solution 함수의 매개변수로 주어집니다.

* s의 길이는 1 이상 100 이하입니다.
* s는 알파벳 소문자로만 구성됩니다.
* k는 200 이하인 자연수입니다.

---
#####return 값 설명

k번째로 큰 팰린드롬 문자열을 return 해주세요.
* 단, s로 만들 수 있는 팰린드롬 수가 k개 미만이면 "NULL"을 return 해주세요.

---
#####예시

| s | k | return |
|---|---|--------|
|"abcba"| 4 | "bcb" |
|"ccddcc"| 7 | "NULL" |

#####예시 설명

예시 #1
"abcba"의 부분 문자열 중 팰린드롬인 문자열을 사전 순으로 나열하면 "a", "abcba", "b", "bcb", "c" 입니다. 이 중 4번째로 큰 팰린드롬은 "bcb"입니다.

예시 #2
"ccddcc"의 부분 문자열 중 팰린드롬인 문자열을 사전 순으로 나열하면 "c", "cc", "ccddcc", "cddc", "d", "dd" 입니다. 팰린드롬인 문자열이 총 6개이므로, 7번째로 큰 팰린드롬은 없습니다. 따라서, "NULL"을 return 합니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def func_a(arr, s):
    return s in arr


def func_b(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True


def func_c(palindromes, k):
    palindromes = sorted(palindromes)
    if len(palindromes) < k:
        return "NULL"
    else:
        return palindromes[k - 1]


def solution(s, k):
    palindromes = []
    length = len(s)
    for start_idx in range(length):
        for cnt in range(1, length - start_idx + 1):
            sub_s = s[start_idx: start_idx + cnt]
            if func_b(sub_s) == True:
                if func_a(palindromes, sub_s) == False:
                    palindromes.append(sub_s)

    answer = func_c(palindromes, k)
    return answer


s1 = "abcba"
k1 = 4
ret1 = solution(s1, k1)

print("solution 함수의 반환 값은", ret1, "입니다.")
# 결과 : solution 함수의 반환 값은 bcb 입니다.

s2 = "ccddcc"
k2 = 7
ret2 = solution(s2, k2)

print("solution 함수의 반환 값은", ret2, "입니다.")
# 결과 : solution 함수의 반환 값은 NULL 입니다.
