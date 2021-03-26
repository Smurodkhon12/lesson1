
# x = [12, 4, 90]
# print(x)
# x.append([300,555])
#
# print(x)

# a = int(input("a ga son kirit"))
# b = int(input("b ga son kirit"))
# c = int(input("c ga son kirit"))

# x = [a, b, c]
# print(x)


# x = []
# for i in range(4):
#     x.append(input("qiymat kiriting"))


# x = []
# for i in range(101):
#    x.append(i)
# print(x)

# x = []
# for i in range(101):
#     x.append(i)
#     if i % 2 != 0:
#       print(i)


# a = int(input("son kirit"))
# b = int(input("son kirit"))
# c = int(input("son kirit"))

# x = (a, b, c)
# print(x)

# y = (c, b, a)
# print(y)



# x = []
# for i in range (101):
#     x.append(i)
#
# for i in x:
#     if  i % 2 != 0:
#         print(i, "= toq")

# x = []
# for i in range(3):
#     x.append(input("x ga element kiriting"))
#
# index = 0
# value = 0
# for i in range(3):
#     if len(x[i]) > value:
#         index = i
#         value = len (x[i])
#
# print(x[index])


# x = [4, 6, 90, 165, 37, 45]
# v = 0
# for i in x:
#     if i > 100:
#         v = i
#         print(v)

# uy ishi 6 dars

# 1

# x = int(input("raqam kirit"))
# li = []
# while x != 0:
#     li.append(x)
#     x = int(input("keyingi raqam kirit"))
#
# print("kiritilgan raqam", li)


# 2

# fib_list = [0, 1]
#
# while fib_list[-1] < 2000:
#     fib_list.append(fib_list[-1] + fib_list[-2])
#
# toq_list = []
# juft_list = []
# for i in fib_list:
#     if i % 2 == 0:
#         juft_list.append(i)
#     else:
#         toq_list.append(i)
#
# print("fibonachi sonlari:", fib_list)
# print("toq_list:", toq_list)
# print("juft_list", juft_list)


# 3

# x = int(input("son kirit"))
# juft_sonlar = []
# toq_sonlar = []
#
# while x != 0:
#     if  x % 2 ==0:
#         juft_sonlar.append(x)
#     else:
#         toq_sonlar.append(x)
#     x = int(input("kiyingi raqamni kiritish"))
#
# print("siz nol kiritdingiz")
# print("juft sonlar:", juft_sonlar)
# print("toq sonlar", toq_sonlar)


# 4

# x = input("malumot kiriting: ")
# raqamlar = []
# satrlar= []
#
# while len(x) > 0:
#     if x.isdigit():
#         raqamlar.append(x)
#     else:
#         satrlar.append(x)
#
#     x =input("keyingi malumotni kiriting: ")
#
# print("siz xech narsa kiritmadingiz!")
# print("raqamlar:", raqamlar )
# print("satrlar", satrlar)


# 5

# x = int(input("raqam kiriting: "))
# li = []
# while x != 0:
#     li.append(x)
#     x = int(input("keyingi raqamni kiriting: "))
#
# print("siz nol kiritdingiz! ")
# print("kiritigan raqamlar ichida eng kichigi: ", min(li))
# print("kiritilgan raqamlar ichida eng kattasi:", max(li))
# print("kiritilgan raqamlar orta arifmetigi:", sum(li) / len(li))




# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
# a = 0
# for i in x:
#     a = a + i
# print(a)


# x = int(input("raqam kiriting:"))
# li = []
# while x != 0:
#     li.append(x)
#     x = int(input("kiyingi raqamni kiriting"))
#
# print("siz nol kiritdingiz! ")
# print("kiritilgan raqamlar ichidagi eng kichigi:", min(li))
# print("kiritilgan raqamlar ichidagi eng kattasi:", max(li))
# print("kiritilgan raqamlar orta arifmetigi:", sum(li) / len(li))



# uy ishi 7 dars
# 1


# satr = input("satr kiriting:")
# numbers = 0
#
# for i in satr:
#     if i.isdigit():
#         numbers += 1
#
# print("kiritilgan sartdagi raqamlar soni:", numbers)

# 2
# a = int(input("raqam"))
# b = 0
#
# while b <100:
#     print("kirit")
#     a = int(input("kir"))
#     b


# 3

# while True:
#     a = int(input("raqam kiriting: "))
#     a = a * a
#     print("kiritilgan raqam kvadrati = ", a)


# 4

# txt = input("satr kiriting:")
# li = []
#
# for i in txt:
#     if i not in li:
#         li.append(i)
#
# print("Satrda bor elemetlar listi:", li)


# print(list(set(list(input("satr kiriting")))))

# txt = "abcderdf"
# print(txt)
# li = list(txt)
# print("txt =", txt)
# print("li", li)

# txt = "aasdafasfasfg"
# print(txt)
# print(list(txt))
# print(set(txt))
# se = set(txt)
# print(type(se))


# 5

# txt = input("satr kiriting: ")
# a = []

# for i in txt:
#     if (txt.count(i) > 1) and (i not in a):
#         print(i)
#         a.append(i)


# txt = input("satr kiriting: ")
# a = []
#
# for i in txt:
#     if (txt.count(i) == 3) and (i not in a):
#         print(i)
#         a.append(i)

# txt = input("satrni kirit: ")
#
# for i in txt:
#     if txt.count(i) == 3:
#         print(i)




