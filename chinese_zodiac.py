#记录生肖，根据年份来判断生肖

#序列
# 定义：有序排列，可以通过下标偏移量访问到它的一个或几个成员
# 包含: 1>>  字符串"abcd"
#       2>>  列表 [0, "abcd"]   ;括号里面内容可变更
#       3>>  元组 ("abc", "def")  ;括号里面内容不可变更
# 基本操作：1>>  切片操作符 [:]   ;序列[0:整数]
#          2>>  成员关系操作符 in、not in    ;对象[not] in 序列
#          3>>  连接操作符 +     ;序列 + 序列
#          4>>  重复操作符 *     ;序列 * 整数

# 一，1.字符串切位操作符[:]
chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'   #引号使用，如果字符串中存在单引号就用双引号，存在双引号就用单引号
print(chinese_zodiac[0]) #输入第一个生肖，第一个要从0开始写
print(chinese_zodiac[0:4]) #访问多个生肖，从0个开始访问到4的前面一个
print(chinese_zodiac[-1]) #最后一个生肖
print(chinese_zodiac[-1:4])#这种会返回空值，最左边索引代表的值比最右边索引代表的值晚出现在序列中

#2.字符串的定义和使用
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = 1996
print(year % 12)
print(chinese_zodiac[year % 12]) #序列里面输入年份除以12后余数，来得出当年是什么属相

# 3.字符串成员关系操作符 in、not in
#'狗' in chinese_zodiac
print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)

# 4.字符串连接操作符 +     ;序列 + 序列
# chinese_zodiac + chinese_zodiac
print(chinese_zodiac + chinese_zodiac)
print(chinese_zodiac + '12345678')

# 5.字符串重复操作符 *     ;序列 * 整数
# chinese_zodiac * 3
print(chinese_zodiac * 3)

#二， 6.元组
# 单个数字比较大小
# >>>(6) > (5)
# >>>ture
# >>>(6) < (5)
# >>>flase
# 多个数字比较大小，可以看成数字叠加，比如下面的是120 > 218
# >>>(1, 20)> (2, 18)
# >>>flase

#介绍几个函数用法，方面下面的程序书写
# a = (1, 3, 5, 7)
# b = 4
# print(filter(lambda x: x < b, a))   # 取出a中小于4的元素 <filter object at 0x0000000002203278>
# print(list(filter(lambda x: x < b, a)))  # 取出a中小于4的元素,并打印出来 [1, 3]
# print(len(list(filter(lambda x: x < b, a))))  # 取出a中小于4的元素个数,并打印出来 2

zodiac_name = (u'摩羯座', u'宝瓶座', u'双鱼座',u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座',
               u'室女座', u'天秤座', u'天蝎座', u'人马座')
zodiac_date = ((1, 19), (1, 20), (2, 18), (2, 19), (3, 20), (3, 21), (4, 19), (4, 20), (5, 20), (5, 21), (6, 21),
               (6, 22), (7, 22), (7, 23), (8, 22), (8, 23), (9, 22), (9, 23), (10, 23), (10, 24), (11, 22),
               (11, 23), (12, 21), (12, 22))
(month, day) = (2, 15)
zodiac_day = filter(lambda x: x < (month, day), zodiac_date)
zodiac_len = len(list(zodiac_day))
print(zodiac_len)
print(zodiac_name[zodiac_len])


# 三.列表
# 列表也可以进行序列的相关操作
a_list = ['abc', 'xyz']
a_list.append('x') #在列表后面加一个元素
print(a_list)
a_list.remove('xyz')#在列表中删除一个元素
print(a_list)


# 列表 切片操作，成员关系操作，连接操作，重复操作
b_list = ['123', '456']
c_list = ['wsd', 'dfd']
print(a_list[0])
print('a' in a_list)
print(b_list + c_list)
print(b_list * 2)
