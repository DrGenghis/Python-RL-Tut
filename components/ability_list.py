class ability_list:
    def __init__(self, abilities):
        self.abilities = abilities

    def use_ability(self, ability):
        self.abilities[ability].use()