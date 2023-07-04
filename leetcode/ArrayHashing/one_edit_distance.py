def isOneEditDistance(s: str, t: str) -> bool:
    
    """
        dabc abc
        
        len(s) == len(t)
            replace
            iterate linearly checking chardiff
            O(n)
        else
            insert/delete
            iterate linearly delete if doesnt match
            O(n)
    """
    if s == t or abs(len(s) - len(t)) > 1:
        return False
        
    if len(s) == len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                return str(s[i+1:]) == str(t[i+1:])
    else:
        s, t = (s, t) if len(s) > len(t) else (t, s)
        print(s, t)
        for i in range(len(s)):
            if i == len(t):
                return True
            if s[i] != t[i]:
                return s[i+1:] == t[i:]

