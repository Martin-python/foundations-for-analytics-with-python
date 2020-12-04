#!/user/bin/env python3
# -*- coding: utf-8 -*-

# Author : Martin
# Date&Time : 2020-11-30 10:10
# Description :

list1 = ['2020', '2019', '2018', '2017', '2016', '2015']
list2 = ['鼠', '猪', '狗', '鸡', '猴', '羊', '马']
list3 = ['子', '亥', '戌', '酉', '申', '未', '午']

list0 = list1 + list2 + list3

for index_value in range(len(list0)):
    print(str(index_value))
    print(list0[index_value])
