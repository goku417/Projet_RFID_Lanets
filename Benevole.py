#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'GreyBerry'
from Liste_Coupons import Liste_Coupons


class Benevole:

    first_name = None
    last_name = None
    rfid = None
    liste_coupons = None

    def __init__(self, first_name, last_name, rfid):
        self.first_name = first_name
        self.last_name = last_name
        self.rfid = rfid
        self.liste_coupons = Liste_Coupons()

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_rfid(self):
        return self.rfid
