__author__ = 'GreyBerry'
from Coupon import Coupon

class Liste_Coupons:

    liste_coupons_repas = None
    liste_coupons_collation = None

    def __init__(self):
        self.liste_coupons_repas = []
        self.liste_coupons_collation = []

    def add_coupon(self, type):
        coupon = Coupon()
        if type == 'collation':
            coupon.set_authorization('collation')
            self.liste_coupons_collation.append(coupon)
        elif type == 'repas':
            coupon.set_authorization('repas')
            self.liste_coupons_repas.append(coupon)

    def remove_coupon(self,type):
        if type == 'collation':
            if len(self.liste_coupons_collation) > 0:
                self.liste_coupons_collation.pop()
        elif type == 'repas':
            if len(self.liste_coupons_repas) > 0:
                self.liste_coupons_repas.pop()

    def get_count_liste(self, type):
        number = 0
        if type == 'collation':
            number = len(self.liste_coupons_collation)
        elif type == 'repas':
            number = len(self.liste_coupons_repas)
        return number