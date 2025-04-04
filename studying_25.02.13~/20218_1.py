n=int(input())
s=[]
e=[]
for i in range(n):
    s.append(input())
for i in range(n):
    e.append(input())
c=0
for i in range(n):
    if s[i]==e[i]:
        c=1
if c==1:
    print("suspicious")
    exit(0)
l=[]
for i in range(n):
    for k in range(n):
        if e[i]==s[k]:
            l.append(k-i)
print(e[l.index(max(l))])