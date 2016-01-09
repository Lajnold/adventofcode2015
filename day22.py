#!/usr/bin/env python3


day22_input = {
    "Hit Points": 71,
    "Damage": 10
}


class Character:
    def __init__(self, hit_points=0, mana=0, damage=0, armor=0):
        self.hit_points = hit_points
        self.mana = mana
        self.damage = damage
        self.armor = armor


class Spell:
    def __init__(self, name, cost, duration, handler):
        self.name = name
        self.cost = cost
        self.duration = duration
        self.handler = handler


class ActiveSpell:
    def __init__(self, spell):
        self.spell = spell
        self.duration = spell.duration


def magic_missile(me, enemy, stage):
    print("Magic missile deals 4 damage")
    enemy.hit_points -= 4

def drain(me, enemy, stage):
    print("Drain deals 2 damage, healing 2")
    enemy.hit_points -= 2
    me.hit_points += 2

def shield(me, enemy, stage):
    if stage == 1:
        me.armor += 7
        print("Shield increases your armor by 7")
    elif stage == 3:
        me.armor -= 7
        print("Shield disappears; armor reduced to {}".format(me.armor))

def poison(me, enemy, stage):
    print("Poison deals 3 damage")
    enemy.hit_points -= 3

def recharge(me, enemy, stage):
    print("Recharge restores 101 mana")
    me.mana += 101

SPELLS = [
    Spell("Magic Missile", 53, 0, magic_missile),
    Spell("Drain", 73, 0, drain),
    Spell("Shield", 113, 6, shield),
    Spell("Poison", 173, 6, poison),
    Spell("Recharge", 229, 5, recharge)
]


def make_me():
    return Character(hit_points=50, mana=500)


def make_enemy():
    return Character(hit_points=day22_input["Hit Points"],
                     damage=day22_input["Damage"])



active_spells = []


def cast_spell(me, enemy, spell):
    print("You cast {}".format(spell.name))

    if spell.duration == 0:
        spell.handler(me, enemy, 1)
    else:
        active_spells.append(ActiveSpell(spell))

    me.mana -= spell.cost


def check_active_spells(me, enemy):
    for sp in active_spells:
        if sp.duration == sp.spell.duration:
            stage = 1
        elif sp.duration > 1:
            stage = 2
        else:
            stage = 3

        sp.spell.handler(me, enemy, stage)
        sp.duration -= 1

        print("Remaining turns for {}: {}".format(sp.spell.name, sp.duration))

        if me.hit_points <= 0 or enemy.hit_points <= 0:
            break

    for i in reversed(range(len(active_spells))):
        if active_spells[i].duration == 0:
            del active_spells[i]


def print_spells():
    print("Spells:")
    for i, spell in enumerate(SPELLS):
        print("{}: {}: cost: {}".format(i + 1, spell.name, spell.cost))


def print_character(name, char):
    print("{}: hit points: {}, mana: {}, armor: {}".format(
          name, char.hit_points, char.mana, char.armor))


def get_spell_input(me):
    while True:
        inp = input("Cast what spell? ")
        try:
            if inp == "?":
                print_spells()
            else:
                num = int(inp)
                if num >= 1 and num <= len(SPELLS):
                    spell = SPELLS[num - 1]
                    if any(x for x in active_spells if x.spell == spell):
                        print("Spell already active")
                    elif me.mana < spell.cost:
                        print("Not enough mana")
                    else:
                        return spell
                else:
                    print("Invalid spell")
        except ValueError:
            print("Invalid spell")


def do_game(before_player_turn):
    while True:
        print()
        print("New fight!")
        print()

        active_spells.clear()
        me = make_me()
        enemy = make_enemy()
        mana_used = 0
        spells_used = []
        turn = 0

        while me.hit_points > 0 and me.mana > SPELLS[0].cost and enemy.hit_points > 0:
            if turn > 0:
                print()

            if turn > 0 and turn % 2 == 0 and before_player_turn:
                before_player_turn(me)

            if me.hit_points <= 0 or enemy.hit_points <= 0:
                break

            check_active_spells(me, enemy)

            if me.hit_points <= 0 or enemy.hit_points <= 0:
                break

            if turn % 2 == 0:
                print_character("You", me)
                print_character("Enemy", enemy)

                spell = get_spell_input(me)
                if spell:
                    cast_spell(me, enemy, spell)
                    mana_used += spell.cost
                    spells_used.append(spell.name)
            else:
                dam = max(1, enemy.damage - me.armor)
                print("Enemy deals {} damage".format(dam))
                me.hit_points -= dam

            turn += 1

        print()
        if me.hit_points > 0 and enemy.hit_points <= 0:
            print("You won!")
        else:
            print("You lost!")

        print()
        print("Spells used: {}".format(spells_used))
        print("Total mana used: {}".format(mana_used))


def part1():
    print_spells()
    do_game(None)

    # You won!
    # Spells used: ['Poison', 'Recharge', 'Shield', 'Poison', 'Recharge', 'Shield', 'Poison', 'Recharge', 'Shield', 'Poison', 'Magic Missile', 'Magic Missile']
    # Total mana used: 1824


def part2():
    def before_player_turn(me):
        print("You lose 1 hit point")
        me.hit_points -= 1

    print_spells()
    do_game(before_player_turn)

    # You won!
    # Spells used: ['Shield', 'Recharge', 'Poison', 'Shield', 'Recharge', 'Poison', 'Shield', 'Recharge', 'Poison', 'Shield', 'Magic Missile', 'Poison', 'Magic Missile']
    # Total mana used: 1937


while True:
    g = input("Easy (1) or hard (2)? ")
    if g == "1":
        part1()
        break
    elif g == "2":
        part2()
        break
    else:
        print("Enter 1 or 2.")
