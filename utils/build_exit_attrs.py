#!/usr/bin/python3
from enum import IntEnum
import json
import sys
sys.path.insert(0, '..')

from gamerules.exit_effect_kind import ExitEffectKind
from gamerules.exit_kind import ExitKind
from utils.generator_utils import *


with open('./json/desc.json') as f:
  DESCS = json.load(f)
with open('./json/lines.json') as f:
  LINES = json.load(f)
with open('./json/objects.json') as f:
  OBJECTS = json.load(f)
with open('./json/roomdesc.json') as f:
  ROOMDESCS = json.load(f)


def maybe_set_desc(desc_id, exit_name, attr_name):
  if not desc_id or desc_id == 0 or desc_id == DEFAULT_MSG_ID:
    return
  desc = lookup_description(desc_id, DESCS, LINES)
  print(f"@set {exit_name}/{attr_name} = {repr(desc)}")
  print('#') 


def make_exit(exit, to_loc, come_out_exit):
  exit_kind = ExitKind(exit['kind'])
  direction = exit['direction']
  direction_letter = direction[0]
  to_room_id = f'room_{to_loc}'
  # req_verb is only used in a single exit - maybe by error?
  # req_verb = exit['req_verb']

  alias = exit['alias']
  if alias:
    exit_names = f"{direction};{direction_letter};{alias}"
  else:
    exit_names = f"{direction};{direction_letter}"

  exit_name = exit_names.split(';')[0]
  print(f"@set {exit_name}/exit_kind = {exit_kind}")
  print('#')
  if exit['auto_look'] == False:
    # True is default auto_look, so only print if it's non-default
    print(f"@set {exit_name}/auto_look = {exit['auto_look']}")
    print('#')

  if alias:
    print(f"@set {exit_name}/password = {repr(alias)}")
    print('#')

  # there are several different flavors of invisible exit
  if (exit_kind == ExitKind.NO_EXIT
    or exit_kind == ExitKind.PASSWORDED
    or exit['hidden']):
    print(f"@lock {exit_name} = view:none()")
    print('#')

  # and several flavors of impassable exit
  if (exit_kind == ExitKind.NO_EXIT
    or exit_kind == ExitKind.PASSWORDED
    or exit['req_alias']
    or exit['hidden']):
    print(f"@lock {exit_name} = traverse:none()")
    print('#')

  # and then there's hidden-but-searchable, too
  if exit['hidden']:
    # TODO: handle 32000 default ?
    hidden_desc = lookup_description(exit['hidden'], DESCS, LINES)
    if hidden_desc:
      print(f"@set {exit_name}/hidden_desc = {repr(hidden_desc)}")
      print('#')
      print(f"@set {exit_name}/hiding = 1")
      print('#')

  # exit effect
  door_effect = exit['door_effect']
  if door_effect:
    exit_effect_value, exit_effect_kind = split_integer(door_effect)
    print(f"@set {exit_name}/exit_effect_kind = {exit_effect_kind}")
    print('#')
    print(f"@set {exit_name}/exit_effect_value = {exit_effect_value}")
    print('#')

  # required object
  obj_req_id = exit['obj_req']
  if obj_req_id:
    obj_req = find_object(OBJECTS, obj_req_id)
    if obj_req:
      print(f"@set {exit_name}/required_object = {repr(obj_req['obj_name'])}")
      print('#')
      if exit_kind == ExitKind.OBJECT_REQUIRED:
        print(f"@lock {exit_name} = traverse:holds({obj_req['obj_name']})")
        print('#')
      elif exit_kind == ExitKind.OBJECT_FORBIDDEN:
        print(f"@lock {exit_name} = traverse: NOT holds({obj_req['obj_name']})")
        print('#')
      elif exit_kind == ExitKind.ONLY_EXISTS_WITH_OBJECT:
        print(f"@lock {exit_name} = traverse:holds({obj_req['obj_name']})")
        print('#')
        print(f"@lock {exit_name} = view:holds({obj_req['obj_name']})")
        print('#')


def main():
  """Command-line script."""
  for roomdesc in ROOMDESCS:
    print('###############################################################################')
    print(f'# {roomdesc["nice_name"]}')
    print('###############################################################################')
    print(f'@tel room_{roomdesc["id"]}')
    print('#')
    for exit in roomdesc['exits']:
      to_loc = exit['to_loc']
      # stupid slot / come_out msg logic
      come_out_exit = None
      come_out_slot = exit['slot']
      if come_out_slot:
        to_room = ROOMDESCS[to_loc-1]
        to_exits = to_room['exits']
        come_out_exit = to_exits[come_out_slot - 1]
      make_exit(exit, to_loc, come_out_exit)


if __name__ == "__main__":
  main()

