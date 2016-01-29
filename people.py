#! /usr/bin/env python
# -*- coding:utf-8 -*-

import d2date


class Person():
    def __init__(self, data=dict()):
        self.name = data.get('name')

        self.life = []
        life = data.get('life')
        self.life = [d2date.parseDate(d) for d in life]

        self.data = data

    def __repr__(self):
        datetexts = (str(d) for d in self.life)
        dates = "-".join(datetexts)
        # dates = "-".join(self.life)
        return "\033[95m%s\033[0m(%s): %s" % (self.name, dates, self.data)
