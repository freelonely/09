#!/usr/bin/python3

import os
import configparser

class configTool(object):
    def __init__(self):
        self.conf=configparser.ConfigParser()

    def getCurrentPath(self):
        return os.path.dirname(os.path.realpath(__file__))

    def buid(self, configPath):
        self.conf.read(configPath)
    def get(self,area,key):
        return self.conf.get(area,key)





