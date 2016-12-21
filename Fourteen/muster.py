import md5
import re

myinput = "yjdafjpo%d"

reg = re.compile(r"(\w)\1\1")

part2 = False

def myhash(xx):
    iters = 1
    if part2:
        iters = 2017
    for i in range(iters):
        n = md5.new()
        n.update(xx)
        xx = n.hexdigest()
    return xx

future = {}
nkeys = 0
def generate():
    global nkeys
    i = -1
    while True:
        i += 1

        if i not in future:
            d = myhash(myinput % i)
        else:
            d = future[i]
            del future[i]

        ma = reg.findall(d)
        if not ma:
            continue

        pat = ma[0] * 5
        for j in range(i + 1, i + 1001):
            if j not in future:
                d2 = myhash(myinput % j)
                future[j] = d2
            else:
                d2 = future[j]

            if pat in d2:
                nkeys += 1
                print "key", nkeys, "index", i, "5-idx", j, "digest", d, "digest2", d2
                if nkeys == 64:
                    print "===>", i
                    return
                yield d
                break

for _ in generate():
    pass
part2 = True
nkeys = 0
for _ in generate():
    pass