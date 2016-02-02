#! /usr/bin/env python
# -*- coding:utf-8 -*-

import yaml


data = {
    "events": [],
    "people": [],
}


def loadFromFile(*filenames):
    global data

    blocks = []
    for filename in filenames:
        with open(filename, 'r') as f:
            blocks += list(yaml.safe_load_all(f))

    files = []
    for block in blocks:
        for a in data:
            data[a] += block.get(a, [])
        files += block.get('files', [])

    for filename in files:
        loadFromFile(filename)

    return [data]
