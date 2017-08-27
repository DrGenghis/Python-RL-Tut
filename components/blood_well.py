class BloodWell:
    def __init__(self):
        self.max_blood = 500
        self.blood = 0

    def add_blood(self, amount):
        self.blood += amount

        if self.blood > self.max_blood:
            self.blood = self.max_blood