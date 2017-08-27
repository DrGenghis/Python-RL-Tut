import libtcodpy as libtcod

from game_messages import Message
from components.modifiers import get_modifier
from random_utils import dice_roll


class Fighter:
	def __init__(self, hitdice, base_damage, brawn, finesse, allure, vitality, armor_class=5, level=1,xp=0):
		self.base_max_hp = ((hitdice + get_modifier(vitality)) * level)
		self.hitdice = hitdice
		self.base_damage = base_damage
		self.hp = self.base_max_hp
		self.base_brawn = brawn
		self.base_finesse = finesse
		self.base_allure = allure
		self.base_vitality = vitality
		self.base_armor_class = armor_class
		self.level = level
		self.xp = xp

	@property
	def brawn(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.brawn_bonus
		else:
			bonus = 0

		return self.base_brawn + bonus

	@property
	def finesse(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.finesse_bonus
		else:
			bonus = 0

		self.base_finesse + bonus

		return self.base_finesse + bonus

	@property
	def allure(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.allure_bonus
		else:
			bonus = 0

		return self.base_allure + bonus

	@property
	def vitality(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.vitality_bonus
		else:
			bonus = 0

		return self.base_vitality + bonus

	@property
	def max_hp(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.max_hp_bonus
		else:
			bonus = 0
			
		return self.base_max_hp + bonus

	@property
	def armor_class(self):
		if self.owner and self.owner.equipment:
			bonus = (self.owner.equipment.ac_bonus + get_modifier(self.finesse))
		else:
			bonus = get_modifier(self.finesse)

		return self.base_armor_class + bonus

	def take_damage(self, amount):
		results = []
	
		self.hp -= amount
		
		if self.hp <= 0:
			results.append({'dead': self.owner, 'xp': self.xp})
			
		return results
		
	def heal(self, amount):
		self.hp += amount
		
		if self.hp > self.max_hp:
			self.hp = self.max_hp

	def attack_chance(self, target):
		if self.owner.equipment:
			if self.owner.equipment.main_hand is not None:
				weapon = self.owner.equipment.main_hand
				if weapon.equippable.weapon_type == 'versatile':  # Versatile weapon can be brawn or finesse
					if self.brawn > self.finesse:
						if (dice_roll('2d6') + get_modifier(self.brawn)) >= target.fighter.armor_class:
							# Hit
							return True
						else:
							# Miss
							return False
					else:
						if (dice_roll('2d6') + get_modifier(self.finesse)) >= target.fighter.armor_class:
							# Hit
							return True
						else:
							# Miss
							return False
				elif weapon.equippable.weapon_type == 'brawn':
					if (dice_roll('2d6') + get_modifier(self.brawn)) >= target.fighter.armor_class:
						# Hit
						return True
					else:
						# Miss
						return False
				elif weapon.equippable.weapon_type == 'finesse':
					if (dice_roll('2d6') + get_modifier(self.finesse)) >= target.fighter.armor_class:
						# Hit
						return True
					else:
						# Miss
						return False
			else:
				if (dice_roll('2d6') + get_modifier(self.brawn)) >= target.fighter.armor_class:
					# Hit
					return True
				else:
					# Miss
					return False
		else:
			if (dice_roll('2d6') + get_modifier(self.brawn)) >= target.fighter.armor_class:
				return True
			else:
				return False

	def attack(self, target):
		results = []

		if self.attack_chance(target):
			if self.owner.equipment:
				if self.owner.equipment.main_hand:
					weapon = self.owner.equipment.main_hand

					if weapon.equippable.weapon_type == 'versatile':
						if self.brawn > self.finesse:
							damage = dice_roll(weapon.equippable.damage) + get_modifier(self.brawn)
						else:
							damage = dice_roll(weapon.equippable.damage) + get_modifier(self.finesse)
					elif weapon.equippable.weapon_type == 'brawn':
						damage = dice_roll(weapon.equippable.damage) + get_modifier(self.brawn)
					elif weapon.equippable.weapon_type == 'finesse':
						damage = dice_roll(weapon.equippable.damage) + get_modifier(self.finesse)
				else:
					damage = dice_roll(self.base_damage) + get_modifier(self.brawn)
			else:
				damage = dice_roll(self.base_damage) + get_modifier(self.brawn)
		else:
			damage = 0

		if damage > 0:
			results.append({'message': Message('{0} attacks {1} for {2} hit points.'.format(self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
			results.extend(target.fighter.take_damage(damage))
		else:
			results.append({'message': Message('{0} attacks {1} but does no damage.'.format(self.owner.name.capitalize(), target.name), libtcod.white)})
			
		return results

	def recalculate_health(self):
		self.base_max_hp = ((self.hitdice + get_modifier(self.base_vitality)) * self.level)