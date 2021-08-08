def isSuffix(x, y) -> bool:
    return x[-len(y):] == y


def lengthOfLongestSubstring(s: str) -> int:
    palabra = s[0]
    for i in range(len(s)):
        if s[i] not isSuffix(palabra, s[i:len(palabra)]):
            palabra = i
    return len(palabra)


print(lengthOfLongestSubstring("abcabcbb"))
