#!/user/bin/env python3
# Author : Martin
# Date&Time : 2020-11-30 10:10
# Description :

import sys
import os
import glob

# 写入文本文件
infor_to_write = ['抚州浪潮计算机科技有限公司',
                  '浪潮（长春）计算机科技有限公司',
                  '浪潮（青岛）电子信息产业有限公司',
                  '浪潮（南宁）计算机科技有限公司']
another_infor_to_write = ['浪潮（厦门）计算机科技有限公司',
                          '贵阳浪潮智能科技有限公司',
                          '浪潮（成都）计算机科技有限公司']
max_index = len(another_infor_to_write)
output_file = sys.argv[1]
filewriter = open(output_file, 'a')
for index_value in range(len(another_infor_to_write)):
    if index_value < (max_index - 1):
        filewriter.write(another_infor_to_write[index_value]+ '\n')
    else:
        filewriter.write(another_infor_to_write[index_value]+ '\n' + '汇总如上')
filewriter.close()
print('success')