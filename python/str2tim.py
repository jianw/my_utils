#!/usr/bin/env python2

# For Arch

import sys

class time:
    def __init__(self, hour, min, sec, ms):
        self._hour = hour
        self._min  = min
        self._sec  = sec
        self._ms   = ms
        
    @property
    def hour(self):
        return self._hour

    @property
    def min(self):
        return self._min

    @property
    def sec(self):
        return self._sec

    @property
    def ms(self):
        return self._ms

    def add(self, a_time):
        self._ms += a_time.ms
        if self._ms >= 1000:
            self._ms -= 1000
            self._sec += 1
        self._sec += a_time.sec
        if self._sec >= 60:
            self._sec -= 60
            self._min += 1
        self._min += a_time.min
        if self._min >= 60:
            self._min -= 60
            self._hour += 1
        self._hour += a_time.hour
        if self._hour >= 24:
            self._hour -= 24

    def diff(self, a_time):
        self._ms -= a_time.ms
        if self._ms < 0:
            self._ms += 1000
            self._sec -= 1
        self._sec -= a_time.sec
        if self._sec < 0:
            self._sec += 60
            self._min -= 1
        self._min -= a_time.min
        if self._min < 0:
            self._min += 60
            self._hour -= 1
        self._hour -= a_time.hour
        if self._hour < 0:
            self._hour += 24

    def gt(self, a_time):
        if self._hour == a_time.hour:
            if self._min == a_time.min:
                if self._sec == a_time.sec:
                    if self._ms == a_time.ms:
                        return False
                    else:
                        return self._ms > a_time.ms
                else:
                    return self._sec > a_time.sec
            else:
                return self._min > a_time.min
        else:
            return self._hour > a_time.hour
        
    def __str__(self):
        return "" + str(self._hour) + ":" + str(self._min) + ":" + str(self._sec) + "," + str(self._ms)

def str2time(a_str):
    print "STR2TIME: " + a_str
    t = a_str.split(':')
    tt = t[2].split(',')
    del t[2]
    t = t + tt
    it = map(int, t)
    return time(it[0], it[1], it[2], it[3])

def minMax(ts):
    max = time(-24, 0, 0, 0)
    min = time(24, 0, 0, 0)
    for t in ts:
        if t.gt(max):
            max = t
        elif min.gt(t):
            min = t
            
    print "\n MIN: "
    print min
    print "\n MAX: "
    print max

def timeAdd(a_time, a_diff):
    at = str2time(a_time)
    at.add(str2time(a_diff))
    return str(at)

def main(argv):
    return


if __name__ == "__main__":
    main(sys.argv)
    
