# -*- coding:UTF-8 -*-
import math

h = float(input('請輸入身高:'))
w = float(input('請輸入體重:'))
bmi = w / math.pow(h/100, 2)
print('BMI計算成果: %.2f' % bmi)
if bmi > 23:
    print("過重")
elif bmi <= 18:
    print("過輕")
else:
    print("正常")
