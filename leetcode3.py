s = input("Enter the chars: ")

sub_s = set()
l = 0
res = 0

for r in range(len(s)):
    while s[r] in sub_s:
        sub_s.remove(s[l])
        l = l+1
    sub_s.add(s[r])
    res = max(res, r - l+1)
    print(res)
    print(sub_s)
print(res)
print(sub_s)
               