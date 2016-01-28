#! /usr/bin/env python
# -*- coding:utf-8 -*-

from six.moves import input
from datetime import datetime
import d2date


handlers = [None, None]

def helloScreen():
    print("Hello")


def byeScreen():
    print("\nBye")


def inputDate():
    text_date = input("Enter the date:\n")
    return datetime.strptime(text_date, "%d.%m.%Y")


def useHandler(id):
    if not id in range(len(handlers)):
        print("Wrong selection")
        return True

    if handlers[id] is None:
        return True

    return handlers[id]()


def mainMenu():
    running = True
    while(running):
        print("1.\tEnter custom date")
        print("2.\tToday")
        print()
        print("0.\tExit")

        try:
            c = int(input("Enter your choice:\t"))
        except(ValueError):
            c = -1
        except(KeyboardInterrupt):
            c = 0

        running = useHandler(c)

def showDate(d):
    print(d.date.strftime("%A, %W week, %j day"))
    tf = "%d %B %Y"
    print("Date\t\t", d.date.strftime(tf))
    print("Gregorian\t", d.getGregorian().strftime(tf))
    print("Julian\t\t", d.getJulian().strftime(tf))
    print("Bizantine\t", d.getByzantine(d2date.CT_BYZ_03).strftime(tf), "\t", d.getByzantine(d2date.CT_BYZ_09).strftime(tf))
    print("AUC\t\t", d.getAUC().strftime(tf))
    print("Armenic\t\t", d.getArmenic().strftime(tf))
    print(d.getChineese())
    print(d.date.strftime(tf))
