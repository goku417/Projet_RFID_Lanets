#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'GreyBerry'

class Coupon:

    collation_authorize = None
    repas_authorize = None

    def __init__(self):
        self.VALUE_COLLATION = 2.00
        self.VALUE_REPAS = 5.00
        self.collation_authorize = False
        self.repas_authorize = False

    def set_authorization(self, type):
        if type == 'collation':
            self.collation_authorize = True
        elif type == 'repas':
            self.repas_authorize = True
        else:
            self.collation_authorize = False
            self.repas_authorize = False

    def get_authorization(self, type):
        authorization = False
        if type == 'collation':
            authorization = self.collation_authorize
        elif type == 'repas':
            authorization = self.repas_authorize
        else:
            authorization = False
        return authorization

    def get_value_coupon(self, type):
        value = None
        if type == 'collation':
            value = self.VALUE_COLLATION
        elif type == 'repas':
            value = self.VALUE_REPAS
        else:
            value = 0
        return value