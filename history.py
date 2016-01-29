#! /usr/bin/env python
# -*- coding:utf-8 -*-

import gui
import sys
import getopt
import yaml
from datetime import datetime
from d2date import D2Date


dates = [None, None]


def showPeople():
    people = []
    print(people)
    with open("people.yml", 'r') as f:
        data = list(yaml.safe_load_all(f))
    print(data)
    for people in data:
        print(people)
        for p in people:
            print('\033[95m' + p["name"] + '\033[0m', p)


def dateCustom():
    d = D2Date(gui.inputDate())
    gui.showDate(d)
    return True


def dateToday():
    d = [
        D2Date(dates[0]),
        D2Date(dates[1]),
    ]
    gui.showDate(d[0])
    gui.showDate(d[1])
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
            dates[0] = datetime.strptime(arg, "%d.%m.%Y")
        elif opt in ("-e", "--end"):
            dates[1] = datetime.strptime(arg, "%d.%m.%Y")
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
