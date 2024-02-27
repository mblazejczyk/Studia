s = "CABCBABBABCDCBAAQWERTREWQZ"

palindromy = []
skip = 0
longest = 0
for i in range(len(s)):
    st = s[i]
    if skip > 0:
        skip -= 1
        continue
    for j in range(i, len(s)):
        if st == s[j]:
            x = i
            y = j
            pali = 0
            while x < y:
                if s[x] == s[y]:
                    pali = 1
                    x += 1
                    y -= 1
                    continue
                else:
                    pali = 0
                    break
        if pali == 1:
            found = ""
            for k in range(i, j + 1):
                found += s[k]
            palindromy.append(found)
            skip = j - i
            if skip > longest: longest = skip
            break

print(palindromy)
print(longest)