#!/usr/bin/env python

class Dumper():
    def dump(self):
        print("rise dumper")
        return "text"

class DumperFactory():
    def create(self):
        print("rise create dumper")
        a = Dumper()
        return a

class Producent:
    def __init__(self, factory):
        self.factory = factory

    def produce(self):
        d = self.factory.create()
        return d.dump()