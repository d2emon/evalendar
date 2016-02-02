#! /usr/bin/env python
# -*- coding:utf-8 -*-

import db_yml
import d2date


events = []


def loadEvents(filename):
    global events

    db_yml.loadFromFile(filename)
    print(db_yml.data)
    event_data = db_yml.data.get('events', [])
    for e in event_data:
        events.append(Event(e))
    return events


class Event():
    def __init__(self, data):
        self.raw = data
        self.title = data.get("title", "Untitled")
        self.date = d2date.D2Date(data.get("date"))
        print(self.raw)

    def __repr__(self):
        return "%s(%s)\t%s" % (self.title, self.date, str(self.raw))
