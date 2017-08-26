from equipment_slots import EquipmentSlots


class Equipment:
	def __init__(self, main_hand=None, off_hand=None):
		self.main_hand = main_hand
		self.off_hand = off_hand
		
	@property
	def max_hp_bonus(self):
		bonus = 0
		
		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.max_hp_bonus
			
		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.max_hp_bonus
			
		return bonus
		
	@property
	def brawn_bonus(self):
		bonus = 0
		
		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.brawn_bonus
			
		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.brawn_bonus
			
		return bonus
		
	@property
	def finesse_bonus(self):
		bonus = 0
		
		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.finesse_bonus
			
		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.finesse_bonus
			
		return bonus

	@property
	def allure_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.allure_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.allure_bonus

		return bonus

	@property
	def vitality_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.vitality_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.vitality_bonus

		return bonus

	@property
	def ac_bonus(self):
		bonus = 0

		return bonus
		
	def toggle_equip(self, equippable_entity):
		results = []
		
		slot = equippable_entity.equippable.slot
		
		if slot == EquipmentSlots.MAIN_HAND:

			if self.main_hand == equippable_entity:
				self.main_hand = None
				results.append({'dequipped': equippable_entity})
			else:
				if self.main_hand:
					results.append({'dequipped': self.main_hand})

					self.main_hand = equippable_entity
					results.append({'equipped': equippable_entity})
				else:
					self.main_hand = equippable_entity
					results.append({'equipped': equippable_entity})
		elif slot == EquipmentSlots.OFF_HAND:
			if self.off_hand == equippable_entity:
				self.off_hand = None
				results.append({'dequipped': equippable_entity})
			else:
				if self.off_hand:
					results.append({'dequipped': self.off_hand})
					
				self.off_hand = equippable_entity
				results.append({'equipped': equippable_entity})
				
		return results