#!/user/bin/env python3
# -*- coding: utf-8 -*-

# Author : Martin
# Date&Time : 2020-12-03 18:25
# Description :

list2 = ['鼠', '猪', '狗', '鸡', '猴', '羊', '马']
list3 = ['子', '亥', '戌', '酉', '申', '未', '午']
list4 = ['1', '2', '3', '4', '5', '6', '7']
dict0 = {}
dict0_keys = dict0.keys()
for index_4 in range(len(list4)):
    if list4[index_4] not in dict0_keys:
        dict0[list4[index_4]] = list2[index_4]

for key, value in dict0.items():
    print("{0:s}:{1:s}".format(key, value))