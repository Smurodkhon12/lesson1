
'''def func(Salom = 'Mehmon', Ismi = 'User', Familyasi =' :)'):
    print(Salom, "Isroil" + Ismi, 'Mehmon' + Familyasi, 'Ergashov')

func('salom', 'Isroil')'''



'''def my_func(*a):
    a = list(a)
    print(a)



my_func(1, 2, 3, 4, 5, 6, 7, 8)'''




'''def my_func(a, b, *c):
    """a b d faqat son bolsin"""
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


my_func(1, 2, 3, 4, 5, 6, 7, 8)'''





'''def my_func(y, *x, n):
    return y * sum(x) / n


print(my_func(2, 2, 4, 545, 352, 24, 52, 42, n=7))
print(my_func(3, 34, 24, 243, 24, 75, n=4))'''




'''a = ("a", "b", "c", "d", "e")

print(*a)


y = ("o", "i", "m", "l", "p")

print(y)'''

# Uyga vazifa

# 1

'''def teskari_satr(txt):
    result = ''
    for i in txt:
        result = i + result
    return result

print(teskari_satr("Saidmurodxon"))
print(teskari_satr('abbos'))'''

# 2

'''def faktorial(n):
    if n == 1:
        return 1

    return faktorial(n-1) * n


print(faktorial(100))'''

# 3

'''def upper_lower_count(txt):
    uppers = 0
    lowers = 0
    for i in txt:
        if i.isupper():
            uppers += 1
        else:
            lowers += 1

    print(f'{uppers=}')
    print(f'{lowers=}')'''

# 4



# 5

# li = ['a', 'b', 'c', 'd', 'e']
#
# print(li[:: - 1])
