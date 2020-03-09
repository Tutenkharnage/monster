from commands.command import Command
from evennia.utils import utils
from gamerules.character_classes import is_valid_character_name


class CmdName(Command):
  """Change your own character name."""
  key = "name"
  aliases = ["nam"]
  locks = "cmd:all()"
  help_category = "Monster"

  def func(self):
    if not self.args:
      self.caller.msg("Usage: name <newname>")
      return
    new_name = self.args.strip()
    if not is_valid_character_name(new_name):
      self.caller.msg(f"{new_name} is not a valid name.")
      return
    self.account.character.name = new_name
    self.caller.msg(f"You are now known as {self.account.character.name}.")


class CmdSheet(Command):
  """Show character sheet."""
  key = "sheet"
  aliases = ["she", "shee"]
  locks = "cmd:all()"
  help_category = "Monster"

  def func(self):
    account = self.account
    character = account.character
    table = self.styled_table(
      "|wCharacter Sheet",
    )
    table.add_row(f"Name         : {utils.crop(account.get_display_name(account), width=25)}")
    table.add_row(f"Class        : {character.character_class().key}")
    table.add_row(f"Alignment    : {character.alignment().name.lower()}")
    table.add_row(f"Size         : {character.size()}'")
    table.add_row(f"Exp/level    : {character.db.xp}/{character.level()}")
    table.add_row(f"Health/Max   : {int(character.db.health)}/{int(character.max_health())}")
    table.add_row(f"Mana/Max     : {character.db.mana}/{character.max_mana()}")
    table.add_row(f"Status       :")
    table.add_row(f"Move delay   : 0")
    table.add_row(f"Move silent  : 0%")
    table.add_row(f"Poison chnce : 0%")
    table.add_row(f"Attack delay : 0")
    table.add_row(f"Weapon usage : {character.total_weapon_use()}%")
    table.add_row(f"Money        : {int(character.carried_gold_amount())}")
    table.add_row(f"Money in Bank: {int(character.db.gold_in_bank)}")
    table.add_row(f"Weapon       : {character.base_weapon_damage()}/{character.random_weapon_damage()}")
    table.add_row(f"Claws        : {character.total_claw_damage()}/{character.random_claw_damage()}")
    table.add_row(f"Armor        : {character.base_armor()}%, {character.deflect_armor()}% deflect")
    table.add_row(f"Spell armor  : {character.spell_armor()}%, {character.spell_deflect_armor()}% deflect")
    self.msg("%s" % table)


