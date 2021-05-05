str = 'she sell sea shell on the sea shore'
print(str)
str = str.strip()  # 除去左右空白
str = str.lstrip()  # 除去左邊空白
str = str.rstrip()  # 除去右邊空白
print('字串長度:', len(str))
print('有幾個s:', str.count('s'))
print('on這個字的位置:', str.find('on'))
print('off這個字的位置:', str.find('off'))
print('有沒有sea這個字:', '有' if str.find('sea') >= 0 else '沒有')
print('有沒有land這個字:', '有' if str.find('land') >= 0 else '沒有')
print('有幾個單字:', str.count(' ') + 1)
# 是否都是英文字(a-z A-Z)
# 小技巧:先利用replace 將中間的空白去除
print('是否都是英文字:', str.replace(' ', '').isalpha())
