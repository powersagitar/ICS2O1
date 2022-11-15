# find the nth occurrence of the divider
def findnth(string, substring, n):
    parts = string.split(substring, n)
    return len(string) - len(parts[-1]) - len(substring)
findnth('foobarfobar akfjfoobar afskjdf foobar', 'foobar', 2)