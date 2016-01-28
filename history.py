#! /usr/bin/env python
# -*- coding:utf-8 -*-

import gui
from d2date import D2Date


def dateCustom():
    d = D2Date(gui.inputDate())
    gui.showDate(d)
    return True


def dateToday():
    d = D2Date()
    gui.showDate(d)
    return True


def stopLoop():
    return False


def main():
    gui.handlers = [
        stopLoop,
        dateCustom,
        dateToday,
    ]

    gui.helloScreen()
    gui.mainMenu()
    gui.byeScreen()

if __name__ == "__main__":
    main()
