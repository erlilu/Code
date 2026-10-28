# for 循环遍历
score_list = [54, 54, 23, 76, 68, 90]
n = 5
# 写法一
for item in score_list:
   print(item)
print('-----------------------------------')
# 写法二
for index in range(len(score_list)):
   print(score_list[index])
print('------------------------------------')
# 写法三
for index, item in enumerate(score_list, start=n):  # 默认为0
    print(index, item, score_list[0])
