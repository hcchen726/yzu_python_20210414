def getChickenAndRabbit(sum, feet):
    '''

    :param sum:83
    :param feet: 240
    :return:
    '''
    if feet/4 <= sum <= feet/2:
        rabbit = (feet - sum * 2) /2
        chicken = sum -rabbit
        return rabbit, chicken
    else:
        print('無法計算')
        return 0, 0

print (getChickenAndRabbit(83, 240))

