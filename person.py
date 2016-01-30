#! /usr/bin/env python
# -*- coding:utf-8 -*-

import yaml
import d2date


def loadPeople(filename):
    people = []
    with open(filename, 'r') as f:
        blocks = list(yaml.safe_load_all(f))
    for block in blocks:
        for p in block:
            people.append(Person(p))
    return people


class Title():
    def __init__(self, data=dict()):
        self.title = data.get('title')

        dates = data.get('dates')
        self.dates = [d2date.parsePeriod(*p) for p in dates]

        self.data = data

    def __repr__(self):
        return "\n".join("\t\033[96m%s\033[0m\t%s" % (self.title, str(t)) for t in self.dates)


class Person():
    def __init__(self, data=dict()):
        self.name = data.get('name')

        life = data.get('life')
        self.life = d2date.parsePeriod(*life)

        titles = data.get('titles', [])
        self.titles = [Title(t) for t in titles]

        self.data = data

    def __repr__(self):
        titles = "\n".join((str(t) for t in self.titles))
        return "\033[95m%s\033[0m\t%s\n%s\n" % (self.name, self.life, titles)
