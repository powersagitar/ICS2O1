def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)
findnth('foobarfobar akfjfoobar afskjdf foobar', 'foobar', 2)

# thinking
# n starts from 0 (eg. the first occurrence is 0)