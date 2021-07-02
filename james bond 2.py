def valid(words, str):
    return str in words

def backtracking(s,l,words):
    if valid(words,s):
        l.append(s)
        return True
    for i in range(1,len(s)):
        if valid(words,s[:i]):
            l.append(s[:i])
            if backtracking(s[i:],l,words):
                return True
            else:
                del l[-1]
    return False

words = set()
f = open("The_Oxford_3000.txt")
s = f.readline()
while len(s)>0:
    words.add(s[:-1].lower())
    s = f.readline()
f.close()

s = "GROWINTERNETMOUNTNORTHRENTSISTERSTORY"
s = s.lower()
l = []
backtracking(s,l,words)
print(l)