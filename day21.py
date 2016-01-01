#!/usr/bin/env python3

ENEMY_STATS = {
    "Hit Points": 109,
    "Damage": 8,
    "Armor": 2
}


shop = {
    "Weapons": [
        ("Dagger", 8, 4, 0),
        ("Shortsword", 10, 5, 0),
        ("Warhammer", 25, 6, 0),
        ("Longsword", 40, 7, 0),
        ("Greataxe", 74, 8, 0)
    ],
    "Armor": [
        ("Leather", 13, 0, 1),
        ("Chainmail", 31, 0, 2),
        ("Splitmail", 53, 0, 3),
        ("Bandedmail", 75, 0, 4),
        ("Platemail", 102, 0, 5)
    ],
    "Rings": [
        ("Damage +1", 25, 1, 0),
        ("Damage +2", 50, 2, 0),
        ("Damage +3", 100, 3, 0),
        ("Armor +1", 20, 0, 1),
        ("Armor +2", 40, 0, 2),
        ("Armor +3", 80, 0, 3)
    ]
}


def allowed_purchases(shop):
    weapons = shop["Weapons"]
    armor = shop["Armor"]
    rings = shop["Rings"]

    # Must buy:
    # * 1 weapon
    # * 0-1 armor
    # * 0-2 rings
    combinations = []
    for w in weapons:
        combinations.append([w])

        for a in armor:
            combinations.append([w, a])

            for i_r1, r1 in enumerate(rings):
                combinations.append([w, a, r1])
                for r2 in rings[i_r1+1:]:
                    combinations.append([w, a, r1, r2])

        for i_r1, r1 in enumerate(rings):
            combinations.append([w, r1])
            for r2 in rings[i_r1+1:]:
                combinations.append([w, r1, r2])

    return combinations


def cost(items):
    return sum(item[1] for item in items)


def make_me(items):
    return {
        "Hit Points": 100,
        "Damage": sum(item[2] for item in items),
        "Armor": sum(item[3] for item in items)
    }


def part1():
    combinations = allowed_purchases(shop)
    combinations.sort(key=cost)

    for items in combinations:
        me = make_me(items)
        me_hp = me["Hit Points"]
        me_damage = me["Damage"]
        me_armor = me["Armor"]

        enemy = dict(ENEMY_STATS)
        enemy_hp = enemy["Hit Points"]
        enemy_damage = enemy["Damage"]
        enemy_armor = enemy["Armor"]

        turn = 0
        while enemy_hp > 0 and me_hp > 0:
            if turn % 2 == 0:
                enemy_hp -= max(1, me_damage - enemy_armor)
            else:
                me_hp -= max(1, enemy_damage - me_armor)

            turn += 1

        if turn % 2 == 1:
            item_names = [item[0] for item in items]
            print("Cheapest win ({}): {}".format(cost(items), item_names))
            break


def part2():
    combinations = allowed_purchases(shop)
    combinations.sort(key=cost, reverse=True)

    for items in combinations:
        me = make_me(items)
        me_hp = me["Hit Points"]
        me_damage = me["Damage"]
        me_armor = me["Armor"]

        enemy = dict(ENEMY_STATS)
        enemy_hp = enemy["Hit Points"]
        enemy_damage = enemy["Damage"]
        enemy_armor = enemy["Armor"]

        turn = 0
        while enemy_hp > 0 and me_hp > 0:
            if turn % 2 == 0:
                enemy_hp -= max(1, me_damage - enemy_armor)
            else:
                me_hp -= max(1, enemy_damage - me_armor)

            turn += 1

        if turn % 2 == 0:
            item_names = [item[0] for item in items]
            print("Most expensive loss ({}): {}".format(cost(items), item_names))
            break


part1()
part2()
