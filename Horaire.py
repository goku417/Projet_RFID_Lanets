__author__ = 'GreyBerry'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

class Horaire:

    commence = None
    termine = None
    FMT = '%H:%M:%S'

    def __init__(self, temps_debut, temps_fin):
        commence = temps_debut
        termine = temps_fin

    def get_temps_commence(self):
        return datetime.strptime(self.commence, self.FMT)

    def get_temps_fin(self):
        return datetime.strptime(self.termine, self.FMT)


