def findroutes(s,fc,dict,route):
    global n
    for a in dict[s]:
        if a==fc:
            n += 1
            print(*route,fc)
            continue
        if a not in route:
            route.append(a)
            findroutes(a,fc,dict,route)
            del route[-1]

f = open("input.txt")
s = f.readline()
cn = 1
while len(s)==2:
    print("CASE ",cn,":",sep="")
    cn += 1
    fc = int(s[:-1])
    dict = {}
    while True:
        s = f.readline()
        if s[0]=='0':
            break
        s = [int(a) for a in s[:-1].split(" ")]
        r,t = s[0],s[1]
        if r in dict:
            dict[r].add(t)
        else:
            dict[r] = set([t])
        if t in dict:
            dict[t].add(r)
        else:
            dict[t] = set([r])
    route = [1]
    n = 0
    findroutes(1,fc,dict,route)
    print("There are ",n," routes from the firestation to streetcorner ",fc,".",sep="")
    s = f.readline()
f.close()