# Project Euler problem 19

import datetime
from dateutil.relativedelta import relativedelta
from projecteuler import time_func

def main():
    start = datetime.datetime(1901, 1, 1)
    end = datetime.datetime(2000, 12, 31)
    #print end - start

    cnt = 0
    while True:
        if end > start:
            if start.weekday() == 6:
                cnt += 1
            start += relativedelta(months=1)
            #print start
        else:
            #print "end"
            break
    print cnt


if __name__ == '__main__':
    time_func(main)
