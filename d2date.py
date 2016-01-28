#! /usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime, timedelta


CT_GREGORIAN = 0
CT_JULIAN = 1


class D2Date():
    def __init__(self, date=None, calendar_type=CT_GREGORIAN):
        if date is None:
            self.date = datetime.today()
        else:
            self.date = date
        self.calendar_type = calendar_type

    def getCentury(self):
        return int(self.date.year / 100) + 1

    def deltaJulian(self):
        print(self.getCentury())
        days = self.getCentury() - 8
        print(days)
        return timedelta(days=days)

    def getGregorian(self):
        mod = self.date
        if self.calendar_type == CT_JULIAN:
            mod = mod + self.deltaJulian()
        return mod

    def getJulian(self):
        mod = self.date
        if self.calendar_type == CT_GREGORIAN:
            mod = mod - self.deltaJulian()
        return mod
