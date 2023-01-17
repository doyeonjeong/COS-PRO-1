# 4회 - 문제 2. 문자열 압축

"""
알파벳 소문자와 대문자로 구성된 문자열을 압축하려 합니다. 압축이란 대표 문자와 대표 문자가 연속되는 개수를 함께 표현하는 것입니다. 이때, 대문자와 소문자는 구분하지 않으며, 대표 문자는 소문자로 표현합니다.
예를 들어, 문자열 "YYYYYbbbBbbBBBMmmM"을 압축하면 "y5b9m4"입니다.
문자열 s가 매개변수로 주어질 때, s를 압축한 문자열을 return 하도록 solution 함수를 작성했습니다. 그러나, 일부 코드가 잘못되어 코드가 바르게 동작하지 않습니다. 주어진 코드가 모든 입력을 바르게 처리하도록 코드를 수정해주세요. 코드는 _**한 줄**_만 수정해야 합니다.

---

#####매개변수 설명

문자열 s가 solution 함수의 매개변수로 주어집니다.

* s의 길이는 1 이상 100000 이하입니다.
* s는 알파벳 소문자, 대문자로만 구성됩니다.
* 알파벳이 반복되는 횟수는 9회 이하로만 주어집니다.
 * 즉, “sssSSSSsss” 와 같은 경우는 주어지지 않습니다.

---

#####return 값 설명

s를 압축한 결과를 return 해주세요.

---

#####예시

| s | return |
|---|--------|
| "YYYYYbbbBbbBBBMmmM" | "y5b9m4" |

#####예시 설명

예시 #1
문제의 예와 같습니다.
"""


def solution(s):
    s = s.lower()
    answer = ""
    previous = s[0]
    counter = 1
    for alphabet in s[1:]:
        if alphabet == previous:
            counter += 1
        else:
            answer += previous + str(counter)
            counter = 1
            previous = alphabet
    answer += previous + str(counter)
    return answer


s = "YYYYYbbbBbbBBBMmmM"
ret = solution(s)

print("solution 함수의 반환 값은", ret, "입니다.")
# 결과 : solution 함수의 반환 값은 y5b9m4 입니다.
