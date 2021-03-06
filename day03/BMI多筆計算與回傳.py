import math


def getBMI(h, w):
    bmi = w / math.pow(h / 100, 2)
    return bmi

def getResult(bmi):
    result = "過輕"
    if 18 < bmi < 23:
        result = "正常"
    elif bmi > 23:
        result = "過重"
    return result

def getBMiAndResult(h, w):
    bmi = getBMI(h, w)
    result = getResult(bmi)
    return bmi, result

bmi1 = getBMI(170, 60)
bmi2 = getBMI(180, 90)
print(bmi1, bmi2)

bmi3, result3 = getBMiAndResult(170, 60)
bmi4, result4 = getBMiAndResult(170, 60)
print("%.2f %s" % (bmi3, result3))
print(bmi4, result4)
