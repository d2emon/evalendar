#! /usr/bin/env python
# -*- coding:utf-8 -*-

import gui
import sys
import getopt
import yaml
import d2date
import person
from datetime import datetime

dates = [
    d2date.D2Date(),
    d2date.D2Date(),
]


def showPeople(dates=[]):
    people = person.loadPeople("people.yml")
    for p in people:
        print(p)


def dateCustom():
    d = d2date.D2Date(gui.inputDate())
    gui.showDate(d)
    return True


def dateToday():
    gui.showDate(dates[0])
    gui.showDate(dates[1])
    showPeople()
    return True


def stopLoop():
    return False


def helpMessage():
    print("history.py [-h|--help][-b|--begin <begindate>][-e|--end <enddate>][-i|--interactive]")
    sys.exit(2)


def prepareDates():
    if dates[1] is None:
        dates[1] = datetime.today()
    if dates[0] is None:
        dates[0] = dates[1]
    if dates[0].date > dates[1].date:
        dates[0], dates[1] = dates[1], dates[0]


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hb:e:i", ["help", "begin=", "end=", "interactive"])
    except(getopt.GetoptError):
        helpMessage()

    global dates
    interactive = False
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            helpMessage()
        elif opt in ("-b", "--begin"):
            dates[0] = d2date.parseDate(arg)
        elif opt in ("-e", "--end"):
            dates[1] = d2date.parseDate(arg)
        elif opt in ("-i", "--interactive"):
            interactive = True

    prepareDates()
    gui.handlers = [
        stopLoop,
        dateCustom,
        dateToday,
    ]

    if not interactive:
        dateToday()
        return True

    gui.helloScreen()
    gui.mainMenu()
    gui.byeScreen()

if __name__ == "__main__":
    main(sys.argv[1:])
