#! /usr/bin/env python
# -*- coding:utf-8 -*-

import gui
import sys
import getopt
import yaml
from d2date import D2Date


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
    d = D2Date()
    gui.showDate(d)
    showPeople()
    return True


def stopLoop():
    return False


def helpMessage():
    print("history.py [-h|--help][-b|--begin <begindate>][-e|--end <enddate>][-i|--interactive]")
    sys.exit(2)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hb:e:i", ["help", "begin=", "end=", "interactive"])
    except(getopt.GetoptError):
        helpMessage()

    dates = [None, None]
    interactive = False
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            helpMessage()
        elif opt in ("-b", "--begin"):
            dates[0] = arg
        elif opt in ("-e", "--end"):
            dates[1] = arg
        elif opt in ("-i", "--interactive"):
            interactive = True

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
