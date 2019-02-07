
def isIsomorphic(s, t):
    s_dict = {}
    t_dict = {}
    for h in range(len(s)):
        if s[h] in s_dict.keys() and s_dict[s[h]] != t[h]:
            return False
        if t[h] in t_dict.keys() and t_dict[t[h]] != s[h]:
            return False
        s_dict[s[h]] = t[h]
        t_dict[t[h]] = s[h]
    return True
