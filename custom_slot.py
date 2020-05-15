from rasa.core.slots import Slot

class MenuOptionSlot(Slot):

    def feature_dimensionality(self):
        return 2

    def as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            if int(self.value) <= 0:
                r[0] = 1.0
            else:
                r[1] = 1.0
        return r