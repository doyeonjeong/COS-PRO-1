
# 4회 - 문제 1. 사전에서 단어찾기

"""
어떤 단어가 XX 사전의 몇 번째 단어인지 알고 싶습니다. XX 사전에는 대문자 알파벳 'A', 'E', 'I', 'O', 'U'를 사용해 만들 수 있는 길이가 5 이하인 모든 단어가 수록되어 있습니다.
예를 들어, 사전의 첫 번째 단어는 "A"이고, 그다음은 "AA"입니다. 마지막 단어는 "UUUUU"입니다.
문자열 word가 매개변수로 주어질 때, word가 사전의 몇 번째 단어인지 return 하도록 solution 함수를 작성했습니다. 그러나, 일부 코드가 잘못되어 코드가 바르게 동작하지 않습니다. 주어진 코드가 모든 입력을 바르게 처리하도록 코드를 수정해주세요. 코드는 _**한 줄**_만 수정해야 합니다.

---

##### 매개변수 설명

문자열 word가 solution 함수의 매개변수로 주어집니다.

* word는 'A', 'E', 'I', 'O', 'U'로만 구성됩니다.
* word의 길이는 5 이하입니다.

---

##### return 값 설명

사전에서 word가 몇 번째 단어인지 return 해주세요.

---

##### 예시

| word | return |
|------|--------|
| "AAAAE" | 6 |
| "AAAE" | 10 |

#####예시 설명

사전엔 단어가 다음과 같이 수록됩니다. "A", "AA", "AAA", "AAAA", "AAAAA", "AAAAE", "AAAAI", "AAAAO", "AAAAU", "AAAE", ...

예시 #1
"AAAAE"는 여섯 번째에 나옵니다.

예시 #2
“AAAE”는 열 번째에 나옵니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

words = []
# cnt = 0


def create_words(lev, s):
    # print(lev, s)
    global words, cnt
    VOWELS = ['A', 'E', 'I', 'O', 'U']
    words.append(s)
    # cnt += 1
    # if cnt > 20: return
    for i in range(0, 5):
        if lev < 5:
            create_words((lev+1), s + VOWELS[i])


def solution(word):
    global words
    words = []
    answer = 0
    create_words(0, '')
    for idx, i in enumerate(words):  # 0부터 시작
        if word == i:
            answer = idx
            break
    return answer


word1 = "AAAAE"
ret1 = solution(word1)

print("solution 함수의 반환 값은", ret1, "입니다.")
# 결과 : solution 함수의 반환 값은 6 입니다.

word2 = "AAAE"
ret2 = solution(word2)

print("solution 함수의 반환 값은", ret2, "입니다.")
# 결과 : solution 함수의 반환 값은 10 입니다.
