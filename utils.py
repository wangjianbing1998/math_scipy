# coding=gbk
import better_exceptions

better_exceptions.hook()

import os

for file in os.listdir('./'):
    print(file)
