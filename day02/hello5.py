# -*- coding:UTF-8 -*-
h = 170
w = 60
bmi = w / (h/100)**2
print("%.3f" % bmi)
print(1/2)
print(5//2)  # 整除(取整數.無條件捨去)
print(5 % 2)  # 餘數

num = 123456789
if num % 2 == 0:
    print("偶數")
else:
    print("奇數")
