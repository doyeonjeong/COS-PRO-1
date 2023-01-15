# 펠린드롬 여부 판별
def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True


def make_palindromes(s):  # if s = "abcba"
    palindromes = set()
    length = len(s)  # 5
    for start_idx in range(length):  # 0, 1, 2, 3, 4
        # 1, 2, 3, 4, 5, 6 : [1:6]
        for cnt in range(1, length - start_idx + 1):
            # start_idx 부터 1글자씩 늘려가며 모든 문자 탐색
            sub_s = s[start_idx: start_idx + cnt]
            if is_palindrome(sub_s) == True:
                palindromes.add(sub_s)
    return palindromes
