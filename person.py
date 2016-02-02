#! /usr/bin/env python
# -*- coding:utf-8 -*-

import yaml
import d2date


def loadPeople(filename):
    people = []
    with open(filename, 'r') as f:
        blocks = list(yaml.safe_load_all(f))[0]
    for block in blocks.get("people", []):
        people.append(Person(block))
    return people


class Title():
    def __init__(self, data=dict()):
        self.title = data.get('title')

        dates = data.get('dates')
        self.dates = [d2date.parsePeriod(*p) for p in dates]

        self.data = data

    def __repr__(self):
        return self.title


class Person():
    def __init__(self, data=dict()):
        self.name = data.get('name')

        life = data.get('life')
        self.life = d2date.parsePeriod(*life)

        titles = data.get('titles', [])
        self.titles = [Title(t) for t in titles]

        self.data = data

    def __repr__(self):
        return self.name
