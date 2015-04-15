# -*- coding: utf-8 -*-

"""
brief:自动生成日期区间的时间戳python代码


bug:不能显示28以上日期

author:zwx

date:2015-4-15

"""
import time

import random

def limit(start,end):

    return(random.randint(start,end))

def connent(num):

    date_result = ""

    for i in range(num):

        year   = limit(2015,2015)

        moon   = limit(1,2)

        day    = limit(1,28)

        hour   = limit(8,23)#0-23

        minute = limit(0,59)

        sec    = limit(0,59)

        date   = str(year)+"-"+str(moon)+"-"+str(day)+" "+str(hour)+":"+str(minute)+":"+str(sec)

        date_result += date+","

    return(date_result)

##num 输出数量

def main(num):

    date_result = connent(num).split(",")

    date = []
