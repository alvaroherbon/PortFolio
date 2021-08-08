def lengthOfLongestSubstring(s):
    palabra = s[0]
    for i in s:
        if not isSuffix(palabra, i):
            palabra = palabra + i
    return len(palabra)


def isSuffix(x: str, y: str):
    return x[-len(y):] == y


print(lengthOfLongestSubstring("abcabcbb"))
