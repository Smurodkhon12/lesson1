# import random
#
#
#
# print(random.randint(1, 10))


# import time
#
# x = 0
# while True:
#     print(x)
#     x = x + 1
#     time.sleep(3)


# import time
#
# print(time.strftime("%H:%M:%S"))
# print(time.strftime("%Y-yil %m-oy %d-kun"))


# import time
#
# x = 0
# while x < 200:
#     print("x ni qiymati =", x)
#     x = x + 1
#     time.sleep(1)


# import time
#
# x = 0
# z = 0
# while x < 20:
#     print("x ni qiymati = ", x,"zni qiymat",z)
#     x = x + 1
#     time.sleep(1)


# x = 5
# y = 7
#
# print(x, "+", y, "=")
#
# if (int(input("kiriting: "))) == (x + y):
#     print("uraaaaaaaaaa!")
# else:
#     print("yutquzdingiz")


# Oyin savol javob   /////   Yangi proyekt!!!

print("ILTIMOS JAVOBLARNI BOSH XARFLARINI KATTA XARFDA YOZING!!! ")


def tarix():
    ball = 0
    x = int(input("Amir Temur nechinchi yil tugilgan: "))

    if x == 1336:
        print("Togri")

        ball += 1
    else:
        print("notogri", 1336, "yilda tugilgan: ")

    alisher = int(input("Alisher Navoiy nechinchi yil tugilgan: "))

    if alisher == 1441:
        print("Togri")

        ball += 1
    else:
        print("notogri", 1441, "yilda tugilgan: ")

    jalolidin = input("Jalolidinning onasini ismi nima bolgan: ")

    if jalolidin == "Oychechak":
        print("togri")

        ball += 1

    else:
        print("Notogri Jalolidinning onasini ismi Oychechak ")

    print("sizda togri javobla soni", ball, "ta")


def geografiya():
    balll = 0

    okean = (input("Dunyodagi eng katta oken qaysi: "))

    if okean == "Tinch":
        print("Togri")

        balll += 1

    else:
        print("Yutqazdingiz Tinch")

    choqqi = (input("Dunyodagi eng kotta choqqi qaysi: "))

    if choqqi == "Everest":
        print("Togri")

        balll += 1

    else:
        print("Yutqazdingiz Everest choqqisi ")

    okean = int(input("Dunyoda nechta okean bor: "))

    if okean == 4:
        print("Togri")

        balll += 1

    else:
        print("Yutqizdingiz 4 ta okean bor")

    daryo = input("Dunyodagi eng uzun daryo qaysi: ")

    if daryo == "Nil":
        print("Togri")

        balll += 1

    else:
        print("Notogri Nil daryosi")

    davlat = input("Dunyodagi eng kichkina davlat qaysi: ")

    if davlat == "Vatikan":

        print("Togri")

        balll += 1

    else:
        print("Notogri Vatikan")

    print("Sizda togri javobla soni", balll, 'ta')


def algebra():
    sdsd = 0
    o = int(input("20 ni 5 ningchi darajasi: "))

    if o == 3200000:
        print("Togri")

        sdsd += 1

    else:
        print("Notogri", 3200000, "boladi")

    print("sizda togri javobla soni", sdsd, "ta")


x = input("Fan tanlang \n 1.Tarix \n 2.Geografiya \n 3.Algebra \n Tanlov = ")

if x == '1':
    tarix()

elif x == "2":
    geografiya()

elif x == "3":
    algebra()

else:
    print("Iltimos!!! \n Togri son kiriting")
