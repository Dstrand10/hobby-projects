
class Character:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.items = []
        self.cost = 0

    def weildItems(self, new_items):
        self.items = new_items.copy()
        if not self.checkItemSetupOkay():
            raise Exception("Item setup not ok!")
        for item in self.items:
            self.damage += item.damage
            self.armor += item.armor
            self.cost += item.cost


    def checkItemSetupOkay(self):
        item_type = list(map(lambda x: x.type, self.items))
        return item_type.count("Weapon") < 2 and item_type.count("Armor") < 2 and item_type.count("Ring") < 3

    def copy(self):
        return self.copy()


class Item:
    def __init__(self, type, name, cost, damage, armor):
        self.type = type
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

# Input data
shop = {
    "Weapons": [
        Item("Weapon", "Dagger", 8, 4, 0),
        Item("Weapon", "Shortsword", 10, 5, 0),
        Item("Weapon", "Warhammer", 25, 6, 0),
        Item("Weapon", "Longsword", 40, 7, 0),
        Item("Weapon", "Greataxe", 74, 8, 0)
    ],
    "Armor": [
        Item("Armor", "Leather", 13, 0, 1),
        Item("Armor", "Chainmail", 31, 0, 2),
        Item("Armor", "Splintmail", 53, 0, 3),
        Item("Armor", "Bandedmail", 75, 0, 4),
        Item("Armor", "Platemail", 102, 0, 5)
    ],
    "Rings": [
        Item("Ring", "Damage +1", 25, 1, 0),
        Item("Ring", "Damage +2", 50, 2, 0),
        Item("Ring", "Damage +3", 100, 3, 0),
        Item("Ring", "Defense +1", 20, 0, 1),
        Item("Ring", "Defense +2", 40, 0, 2),
        Item("Ring", "Defense +3", 80, 0, 3),
    ]
}



def fight(Daniel, monster):
    while True:
        # Daniel attack
        if Daniel.damage > monster.armor:
            monster.health += (monster.armor - Daniel.damage)
        else:
            monster.health -= 1
        if monster.health <= 0:
            break
        # Monster attack
        if monster.damage > Daniel.armor:
            Daniel.health += (Daniel.armor - monster.damage)
        else:
            Daniel.health -= 1
        if Daniel.health <= 0:
            break


min_cost = 1000000
max_cost = 0
starting_monster = Character("Matilda", 109, 8, 2) # Input data
starting_Daniel = Character("Daniel", 100, 0, 0)
for idx_weapon in [0, 1, 2, 3, 4]:
    for idx_armor in [None, 0, 1, 2, 3, 4]:
        for idx_left_ring in [None, 0, 1, 2, 3, 4, 5]:
            for idx_right_ring in [None, 0, 1, 2, 3, 4, 5]:
                if idx_left_ring is not None and idx_left_ring == idx_right_ring:
                    continue
                monster = Character("Matilda", 109, 8, 2)
                Daniel = Character("Daniel", 100, 0, 0)
                items = []
                items.append(shop["Weapons"][idx_weapon])
                if idx_armor is not None:
                    items.append(shop["Armor"][idx_armor])
                if idx_left_ring is not None:
                    items.append(shop["Rings"][idx_left_ring])
                if idx_right_ring is not None:
                    items.append(shop["Rings"][idx_right_ring])
                Daniel.weildItems(items)
                fight(Daniel, monster)
                if Daniel.health > monster.health and Daniel.cost < min_cost:
                    min_cost = Daniel.cost
                    min_item = items
                if Daniel.health < monster.health and Daniel.cost > max_cost:
                    max_cost = Daniel.cost
                    max_item = items

print("Answer 1: " + str(min_cost))
print("Answer 2: " + str(max_cost))
