talia = [2, 3, 7, 9, 10, 6, 8, 4]

def f(a):
    for i in range(1, len(a)):
        k = a[i]
        j = i - 1
        while j >= 0 and k < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = k
    return a

print(f(talia))