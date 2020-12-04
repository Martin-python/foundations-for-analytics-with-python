#!/user/bin/env python3
# -*- coding: utf-8 -*-

# Author : Martin
# Date&Time : 2020-12-03 19:01
# Description :

list5 = [['浪','潮','济','南'], ['容', '诚', '广', '州']]

for list5_n in list5:
    max_index = len(list5_n)
    output = ''
    for index_value in range(len(list5_n)):
        if index_value < (max_index-1):
            output += str(list5_n[index_value])+','
        else:
            output += str(list5_n[index_value])+'\n'

print(output)
