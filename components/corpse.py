import libtcodpy as libtcod

from game_messages import Message


class FeedableCorpse:
    def __init__(self):
        self.age = 0
        self.blood = 10

        self.name = 'Fresh'

def age_up(entities):
    for i in entities:
        if i.corpse:
            i.corpse.age += 1

            if i.corpse.age > 9:
                i.corpse.name = 'Dessicated'
                i.corpse.blood = 0
                i.color = libtcod.gray
            elif i.corpse.age > 4:
                i.corpse.name = 'Bloated'
                i.corpse.blood = 5
                i.color = libtcod.darker_red

def drain(player, corpse, message_log):
    player.blood_well.add_blood(corpse.blood)

    corpse.age = 10
    corpse.blood = 0
    corpse.owner.color = libtcod.gray