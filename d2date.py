#! /usr/bin/env python
# -*- coding:utf-8 -*-
import flexidate
from datetime import datetime, timedelta
from dateutil import relativedelta


CT_GREGORIAN = 0
CT_JULIAN = 1
CT_BYZ_03 = 2
CT_BYZ_09 = 3
CT_AUC = 4
CT_ARMENIC = 5

DATE_FORMAT = "%d.%m.%Y"


def parseDate(date=None):
    if date is None:
        date = datetime.today()
    return D2Date(flexidate.parse(date))


def parsePeriod(*dates):
    return D2Period([parseDate(d) for d in dates])


class D2Period():
    def __init__(self, dates=[None, None]):
        if len(dates) < 1:
            dates.append(None)
        if len(dates) < 2:
            dates.append(None)
        self.beginDate, self.endDate = dates[:2]
        self.setupDates()

    def setupDates(self):
        if (self.beginDate is not None) or (self.endDate is None):
            return
        if self.beginDate.date > self.endDate.date:
            self.beginDate, self.endDate = self.endDate, self.beginDate

    def getYears(self, date=None):
        if date is None:
            date = D2Date()
        if self.beginDate is None:
            return 0
        if self.endDate is None:
            self.endDate = date
        return relativedelta.relativedelta(self.endDate.date, self.beginDate.date).years

    def fromFirst(self, date=None):
        if date is None:
            date = D2Date()
        if self.beginDate is None:
            return 0
        return relativedelta.relativedelta(date.date, self.beginDate.date).years

    def isInPeriod(self, date):
        fit = True
        if self.beginDate is not None:
            fit = (date.date > self.beginDate.date)
        if self.endDate is not None:
            fit = (date.date < self.endDate.date)
        return fit

    def isIntersect(self, period):
        fit = True
        if self.beginDate is not None:
            fit = (period.endDate.date > self.beginDate.date)
        if self.endDate is not None:
            fit = (period.beginDate.date < self.endDate.date)
        return fit

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        datetexts = [[str(d), "..."][d is None] for d in [self.beginDate, self.endDate]]
        return ("%s (%d)" % ("-".join(datetexts), self.getYears()))


class D2Date():
    def __init__(self, date=None, calendar_type=CT_GREGORIAN):
        if date is None:
            self.date = flexidate.FlexiDate()
        else:
            self.date = date
        self.calendar_type = calendar_type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.date.strftime(DATE_FORMAT)

    def getCentury(self):
        return int(self.date.year / 100) + 1

    def is_leap(self):
        if self.calendar_type == CT_GREGORIAN:
            if (self.date.year % 400) == 0:
                return True
            elif (self.date.year % 100) == 0:
                return False
        return (self.date.year % 4) == 0

    def deltaJulian(self):
        c = self.getCentury()
        days = c - int(c / 4) - 3
        if ((self.date.year % 400) != 0) and (self.date.month > 2) and (self.date.day < days):
            days -= 1
        return timedelta(days=days)

    def deltaByzantine(self, style=CT_BYZ_09):
        j = self.getJulian()
        if style == CT_BYZ_03:
            years = 5507
            if j.month >= 3:
                years += 1
        elif style == CT_BYZ_09:
            years = 5508
            if j.month >= 9:
                years += 1
        else:
            years = 0

        return relativedelta.relativedelta(years=years)

    def deltaAUC(self):
        g = self.getGregorian()
        years = 752
        if ((g.month == 3) and (g.day >= 4)) or (g.month > 3):
            years += 1
        return relativedelta.relativedelta(years=years)

    def deltaArmenic(self):
        g = self.getGregorian()
        years = -551
        return relativedelta.relativedelta(years=years)

    def getGregorian(self):
        if self.calendar_type == CT_GREGORIAN:
            return self.date

        mod = self.date + self.deltaJulian()
        return mod

    def getJulian(self):
        if self.calendar_type == CT_JULIAN:
            return self.date

        mod = self.date - self.deltaJulian()
        return mod

    def getByzantine(self, style=CT_BYZ_09):
        if self.calendar_type == style:
            return self.date
        mod = self.getJulian()
        mod += self.deltaByzantine(style)
        return mod

    def getAUC(self):
        if self.calendar_type == CT_AUC:
            return self.date

        mod = self.getGregorian() + self.deltaAUC()
        return mod

    def getArmenic(self):
        if self.calendar_type == CT_ARMENIC:
            return self.date

        mod = self.getGregorian() + self.deltaArmenic()
        return mod

    def getChineese(self):
        elements = [
            "Wood",
            "Fire",
            "Earth",
            "Metal",
            "Water"
        ]
        colors = [
            "Green",
            "Red",
            "Yellow",
            "White",
            "Blue"
        ]
        animals = [
            "Rat",
            "Ox",
            "Tiger",
            "Rabbit",
            "Dragon",
            "Snake",
            "Horse",
            "Goat",
            "Monkey",
            "Rooster",
            "Dog",
            "Pig"
        ]
        yin_yang = [
            "Yang",
            "Yin",
        ]
        year = (self.date.year % 60) - 4
        animal_id = year % 12
        element_id = int((year % 10) / 2)
        yin = year % 2
        return "%s %s %s %s" % (yin_yang[yin], colors[element_id], elements[element_id], animals[animal_id])
