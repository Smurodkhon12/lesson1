# from random import * ## tasodifiy son yoki harfni tanlash
# tahmin = ""
# parol = input("buziladigan parolni kiriting>>")
# xarflar=["a","b",'c','d','e','f','g',"h","j","k",'l','m','n','o','p','q','r','s','t','u','w','x','v','z','y']
# while(tahmin != parol):
#     tahmin = ""
#     for harf in range(len(parol)):
#         tahmin_xarf=xarflar[randint(0, 25)]
#         tahmin=str(tahmin_xarf)+str(tahmin)
#         print(tahmin)
# print("parol buzib kirildi")
# tugatish = input("parol:<<{tahmin}>> Dasturdan chiqish uchun istalgan tugmani bosing")






# di = {"a": "salom" }
# print(di["a"])


# user = {"ismi":"Ahmad",
#         "yoshi": 28,
#         "yashash joyi": "Toshkent",
#         "jinsi": "erkak"}
# print(user["ismi"])
# print(user["yoshi"])
# print(user["yashash joyi"])
# print(user["jinsi"])
#
# user["ismi"] = "joxa"
# print(user["ismi"])


# x = {"ismi":input("ismi kiriting"),
#      "yoshi" : input("yoshini kiriting"),
#      "jinsi": input("jinsini kiriting"),
#      "yashash joyi": input("yashash joyini kiriting")}
# print(x)

# x = {0:'nol',
#      1: 'bir',
#      2: 'ikki',
#      3: 'uch',
#      4: 'tort',
#      5: 'besh',
#      6: 'olti',
#      7: 'yetti',
#      8: 'sakkiz',
#      9: 'toqqiz'}
# print(x)

# di = {"ismi": "joxa",
#        "yoshi":36}
#
# print(di)
# di.update({"familyasi": "abraham",
#            "yashash joyi":"toshkent",
#             "yoshi": 50})
# print(di)
#
# for kalit, qiymat in di.items():
#     print(kalit, " = ", qiymat)




# uyga vazifa

# 1

# x = {"ismi":input("ismini kiriting"),
#      "familasi":input("familasini kiriting"),
#      "yoshi":input("yoshini kiriting"),
#      "kasbi" :input("kasbini kiriting"),
#      "yashash joyi" :input("yashash joyini kiriting"),
#      "telefon raqami" :input("telefon raqamini kiriting")}
#
# print(x)


# 2


# 3

# txt = input("satr kiriting")
# li = []
# di = {}
# for i in txt:
#      li.append(i)
# di = {i: li.count(i) for i in li}
# print(di)


# 4

# a = []
# b = {}
# for i in range (1001):
#      i = i* i
#      a.append(i)
# for i in range (1001):
#      b[i]=a[i]
# for kalit,qiymat in b.items():
#      print(kalit, "=", qiymat)



dic = {}

for i in range(1, 1000):
     dic[i] = i * i

print(dic)


# 5

dic = {}
