class Equippable:
	def __init__(self, slot, brawn_bonus=0, finesse_bonus=0, allure_bonus=0, vitality_bonus=0, max_hp_bonus=0, damage=0, weapon_type=None):
		self.slot = slot
		self.brawn_bonus = brawn_bonus
		self.finesse_bonus = finesse_bonus
		self.allure_bonus = allure_bonus
		self.vitality_bonus = vitality_bonus
		self.max_hp_bonus = max_hp_bonus
		self.damage = damage
		self.weapon_type = weapon_type