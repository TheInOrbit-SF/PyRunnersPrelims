import math

class TrigEnhancer:
    @staticmethod
    def sin_deg(x):
        return math.sin(math.radians(x))

    @staticmethod
    def sec_deg(x):
        return 1 / math.cos(math.radians(x))
