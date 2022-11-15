# find the nth occurrence of the divider
def findnth(string, substring, n):
    parts = string.split(substring, n)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)
findnth('foobarfobar akfjfoobar afskjdf foobar', 'foobar', 2)