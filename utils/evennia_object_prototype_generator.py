#!/usr/bin/python3
import json
import sys
sys.path.insert(0, '..')

from typeclasses.object_effect_kind import ObjectEffectKind
from typeclasses.object_kind import ObjectKind


DESC_FILE = './json/desc.json'
LINES_FILE = './json/lines.json'
OBJECT_FILE = './json/objects.json'


def parse_parm(i):
  """Parse a parm integer into the effect and effectnum."""
  return (i % 100, int(i / 100))


def lookup_effect(obj, effect):
  for parm in obj['parms']:
    eff, eff_num = parse_parm(parm)
    if eff == effect:
      return eff_num


def camel_case(s):
  """Convert an object name to a useful python class name.

  E.g., 'Hammer of the gods' => 'HammerOfTheGods'
  """
  s = s.strip()
  done = False
  chars = []
  idx = 0
  s_len = len(s)
  while not done:
    c = s[idx]
    if idx == 0:
      chars.append(c.upper())
      idx = idx + 1
    elif c == ' ':
      chars.append(s[idx+1].upper())
      idx = idx + 2
    elif c == "'":
      # skip quote
      idx = idx + 1
    else:
      chars.append(c)
      idx = idx + 1
    if idx >= s_len:
      done = True
  return ''.join(chars)


def snake_case(s):
  """Convert an object name to a snake case.

  E.g., 'Hammer of the gods' => 'HAMMER_OF_THE_GODS'
  """
  s = s.strip()
  chars = []
  for c in s:
    if c == ' ' or c == '-':
      chars.append('_')
    elif c == "'":
      pass
    else:
      chars.append(c.upper())
  return ''.join(chars)


def escaped(s):
  return s.replace('"', '\\"')


def lookup_description(id, descs, lines):
  if not id:
    return None
  elif id > 0:
    # use descs
    desc_idx = id - 1
    # TODO: special handling for default description id 32000
    if desc_idx < len(descs):
      return escaped(' '.join(descs[desc_idx]['lines']))
  elif id < 0:
    # use lines
    line_idx = -id -1
    if line_idx < len(lines):
      return escaped(lines[line_idx]['line'])
  return None


def output_blands(objs, descs, lines):
  print("""#
# 'Bland' objects
#

BASE_BLAND = {
  'typeclass': 'typeclasses.objects.Bland',
  'key': 'base_bland',
  'desc': 'A bland object.',
}
""")
  for obj in objs:
    obj_name = obj['obj_name']
    print(f"{snake_case(obj_name)} = {{")
    # TODO: add better quote escaping for key and desc
    print(f"  'key': \"{obj_name}\",")
    print("  'prototype_parent': 'base_bland',")
    desc = lookup_description(obj['examine'], descs, lines)
    if desc:
      print(f"  'desc': \"{desc}\",")
    print(f"  'weight': {obj['weight']},")
    print(f"  'worth': {obj['worth']},")
    print('}')
    print()


def output_scrolls(objs, descs, lines):
  print("""#
# Scroll objects
#

BASE_SCROLL = {
  'typeclass': 'typeclasses.objects.Scroll',
  'key': 'base_scroll',
  'desc': 'A scroll.',
}
""")
  for obj in objs:
    obj_name = obj['obj_name']
    # TODO: figure out effects
    # ??? = lookup_effect(obj, ObjectEffectKind.???) or 0
    print(f"{snake_case(obj_name)} = {{")
    print(f"  'key': \"{obj_name}\",")
    print("  'prototype_parent': 'base_scroll',")
    desc = lookup_description(obj['examine'], descs, lines)
    if desc:
      print(f"  'desc': \"{desc}\",")
    print(f"  'weight': {obj['weight']},")
    print(f"  'worth': {obj['worth']},")
    print('}')
    print()


def output_wands(objs, descs, lines):
  print("""#
# Wand objects
#

BASE_WAND = {
  'typeclass': 'typeclasses.objects.Wand',
  'key': 'base_wand',
  'desc': 'A wand.',
}
""")
  for obj in objs:
    obj_name = obj['obj_name']
    # TODO: figure out effects
    # ??? = lookup_effect(obj, ObjectEffectKind.???) or 0    
    print(f"{snake_case(obj_name)} = {{")
    print(f"  'key': \"{obj_name}\",")
    print("  'prototype_parent': 'base_wand',")
    desc = lookup_description(obj['examine'], descs, lines)
    if desc:
      print(f"  'desc': \"{desc}\",")
    print(f"  'weight': {obj['weight']},")
    print(f"  'worth': {obj['worth']},")
    print('}')
    print()


def output_missiles(objs, descs, lines):
  print("""#
# Missile objects
#

BASE_MISSILE = {
  'typeclass': 'typeclasses.objects.Missile',
  'key': 'base_missile',
  'desc': 'A missile.',
}
""")
  for obj in objs:
    obj_name = obj['obj_name']
    # TODO: figure out effects
    # ??? = lookup_effect(obj, ObjectEffectKind.???) or 0    
    print(f"{snake_case(obj_name)} = {{")
    print(f"  'key': \"{obj_name}\",")
    print("  'prototype_parent': 'base_missile',")
    desc = lookup_description(obj['examine'], descs, lines)
    if desc:
      print(f"  'desc': \"{desc}\",")
    print(f"  'weight': {obj['weight']},")
    print(f"  'worth': {obj['worth']},")
    print('}')
    print()


def output_missile_launchers(objs, descs, lines):
  print("""#
# Missile launcher objects
#

BASE_MISSILE_LAUNCHER = {
  'typeclass': 'typeclasses.objects.MissileLauncher',
  'key': 'base_missile_launcher',
  'desc': 'A missile launcher.',
}
""")
  for obj in objs:
    obj_name = obj['obj_name']
    # TODO: figure out effects
    # ??? = lookup_effect(obj, ObjectEffectKind.???) or 0    
    print(f"{snake_case(obj_name)} = {{")
    print(f"  'key': \"{obj_name}\",")
    print("  'prototype_parent': 'base_missile_launcher',")
    desc = lookup_description(obj['examine'], descs, lines)
    if desc:
      print(f"  'desc': \"{desc}\",")
    print(f"  'weight': {obj['weight']},")
    print(f"  'worth': {obj['worth']},")
    print('}')
    print()


def output_spellbooks(objs, descs, lines):
  print("""#
# Spellbook objects
#

BASE_SPELLBOOK = {
  'typeclass': 'typeclasses.objects.Spellbook',
  'key': 'base_spellbook',
  'desc': 'A spellbook.',
}
""")
  for obj in objs:
    obj_name = obj['obj_name']
    # TODO: figure out effects
    # ??? = lookup_effect(obj, ObjectEffectKind.???) or 0    
    print(f"{snake_case(obj_name)} = {{")
    print(f"  'key': \"{obj_name}\",")
    print("  'prototype_parent': 'base_spellbook',")
    desc = lookup_description(obj['examine'], descs, lines)
    if desc:
      print(f"  'desc': \"{desc}\",")
    print(f"  'weight': {obj['weight']},")
    print(f"  'worth': {obj['worth']},")
    print('}')
    print()


def output_banking_machines(objs, descs, lines):
  print("""#
# Banking machine objects
#

BASE_BANKING_MACHINE = {
  'typeclass': 'typeclasses.objects.BankingMachine',
  'key': 'banking machine',
  'desc': 'A banking machine.',
}
""")
  for obj in objs:
    obj_name = obj['obj_name']
    # TODO: figure out effects
    # ??? = lookup_effect(obj, ObjectEffectKind.???) or 0        
    print(f"{snake_case(obj_name)} = {{")
    print(f"  'key': \"{obj_name}\",")
    print("  'prototype_parent': 'base_banking_machine',")
    desc = lookup_description(obj['examine'], descs, lines)
    if desc:
      print(f"  'desc': \"{desc}\",")
    print(f"  'weight': {obj['weight']},")
    print(f"  'worth': {obj['worth']},")
    print('}')
    print()


def output_weapons(objs, descs, lines):
  print("""#
# Weapons
#

BASE_WEAPON = {
  'typeclass': 'typeclasses.objects.Weapon',
  'key': 'base_weapon',
  'attack_speed': 0,
  'base_damage': 0,
  'desc': 'A weapon.',
  'equip_slot': 1,
  'random_damage': 0,
  'weight': 0,
  'worth': 0
}
""")
  for obj in objs:
    obj_name = obj['obj_name']
    base_damage = lookup_effect(obj, ObjectEffectKind.WEAPON_BASE_DAMAGE) or 0
    random_damage = lookup_effect(obj, ObjectEffectKind.WEAPON_RANDOM_DAMAGE) or 0
    attack_speed = lookup_effect(obj, ObjectEffectKind.ATTACK_SPEED) or 0
    print(f"{snake_case(obj_name)} = {{")
    # TODO: add better quote escaping for key and desc
    print(f"  'key': \"{obj_name}\",")
    print("  'prototype_parent': 'base_weapon',")
    print(f"  'attack_speed': {attack_speed},")
    print(f"  'base_damage': {base_damage},")
    desc_idx = obj['examine'] - 1
    if desc_idx >= 0 and desc_idx < len(descs):
      # TODO: special handling for 'default' descript 32000
      desc = escaped(' '.join(descs[desc_idx]['lines']))
      print(f"  'desc': \"{desc}\",")
    print(f"  'equip_slot': {obj['wear']},")
    # TODO: handle line_desc? looks mostly dead
    print(f"  'random_damage': {random_damage},")
    print(f"  'weight': {obj['weight']},")
    print(f"  'worth': {obj['worth']},")
    print('}')
    print()


def output_armors(objs, descs, lines):
  print("""#
# Armor
#

BASE_ARMOR = {
  'typeclass': 'typeclasses.objects.Armor',
  'key': 'base_armor',
  'base_armor': 0,
  'deflect_armor': 0,
  'desc': 'An armor.',
  'equip_slot': 4,
  'spell_armor': 0,
  'spell_deflect_armor': 0,
  'weight': 0,
  'worth': 0  
}
""")
  for obj in objs:
    obj_name = obj['obj_name']
    base_armor = lookup_effect(obj, ObjectEffectKind.BASE_ARMOR) or 0
    deflect_armor = lookup_effect(obj, ObjectEffectKind.DEFLECT_ARMOR) or 0
    spell_armor = lookup_effect(obj, ObjectEffectKind.SPELL_ARMOR) or 0
    spell_deflect_armor = lookup_effect(obj, ObjectEffectKind.SPELL_DEFLECT_ARMOR) or 0
    print(f"{snake_case(obj_name)} = {{")  
    # TODO: add better quote escaping for key and desc
    print(f"  'key': \"{obj_name}\",")
    print("  'prototype_parent': 'base_armor',")
    print(f"  'base_armor': {base_armor},")  
    print(f"  'deflect_armor': {deflect_armor},")  
    desc_idx = obj['examine'] - 1
    if desc_idx >= 0 and desc_idx < len(descs):
      # TODO: special handling for 'default' descript 32000
      desc = escaped(' '.join(descs[desc_idx]['lines']))
      print(f"  'desc': \"{desc}\",")
    print(f"  'equip_slot': {obj['wear']},")
    # TODO: handle line_desc? looks mostly dead
    print(f"  'spell_armor': {spell_armor},")  
    print(f"  'spell_deflect_armor': {spell_deflect_armor},")  
    print(f"  'weight': {obj['weight']},")
    print(f"  'worth': {obj['worth']},")
    print('}')
    print()


def output_other_equipment(objs, descs, lines):
  print("""#
# other equipment
#

BASE_EQUIPMENT = {
  'typeclass': 'typeclasses.objects.Equipment',
  'key': 'base_equipment',
  'desc': 'An equipment.',
  'equip_slot': 0,
  'weight': 0,
  'worth': 0
}
""")
  for obj in objs:
    obj_name = obj['obj_name']
    print(f"{snake_case(obj_name)} = {{")
    # TODO: add better quote escaping for key and desc
    print(f"  'key': \"{obj_name}\",")
    print("  'prototype_parent': 'base_equipment',")
    desc = lookup_description(obj['examine'], descs, lines)
    if desc:
      print(f"  'desc': \"{desc}\",")
    print(f"  'equip_slot': {obj['wear']},")
    print(f"  'weight': {obj['weight']},")
    print(f"  'worth': {obj['worth']},")
    print('}')
    print()


def main():
  """Command-line script."""
  with open(DESC_FILE) as f:
    descs = json.load(f)
  with open(LINES_FILE) as f:
    lines = json.load(f)
  with open(OBJECT_FILE) as f:
    objects = json.load(f)

  # divide objects by kind
  obj_by_kind = {}
  for obj in objects:
    obj_by_kind.setdefault(obj['kind'], []).append(obj)
  for arr in obj_by_kind.values():
    arr.sort(key=lambda x: x['obj_name'].upper())

  # subdivide equipment into weapons, armor, and other
  equip = obj_by_kind.pop(ObjectKind.EQUIPMENT)
  equip_weapons = []
  equip_armors = []
  equip_other = []
  for obj in equip:
    if (lookup_effect(obj, ObjectEffectKind.WEAPON_BASE_DAMAGE)
      or lookup_effect(obj, ObjectEffectKind.WEAPON_RANDOM_DAMAGE)):
      equip_weapons.append(obj)
    elif (lookup_effect(obj, ObjectEffectKind.BASE_ARMOR)
      or lookup_effect(obj, ObjectEffectKind.DEFLECT_ARMOR)
      or lookup_effect(obj, ObjectEffectKind.SPELL_ARMOR)):
      equip_armors.append(obj)
    else:
      # TODO: we'll need to further subcategorize these (scrolls, etc)
      equip_other.append(obj)

  print("""#
# Generated object prototypes
#
""")
  output_blands(obj_by_kind[ObjectKind.BLAND], descs, lines)
  output_weapons(equip_weapons, descs, lines)
  output_armors(equip_armors, descs, lines)
  output_other_equipment(equip_other, descs, lines)
  output_scrolls(obj_by_kind[ObjectKind.SCROLL], descs, lines)
  output_wands(obj_by_kind[ObjectKind.WAND], descs, lines)
  output_missiles(obj_by_kind[ObjectKind.MISSILE], descs, lines)
  output_missile_launchers(obj_by_kind[ObjectKind.MISSILE_LAUNCHER], descs, lines)
  output_spellbooks(obj_by_kind[ObjectKind.SPELLBOOK], descs, lines)
  output_banking_machines(obj_by_kind[ObjectKind.BANKING_MACHINE], descs, lines)


if __name__ == "__main__":
  main()