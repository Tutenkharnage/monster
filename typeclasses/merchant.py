from evennia.utils import evtable
from evennia.prototypes.spawner import spawn
from typeclasses.objects import Object


class Merchant(Object):
  def at_object_creation(self):
    super().at_object_creation()
    self.sticky = True
    self.db.for_sale_keys = []
    # spawn("axe")[0].location = self
    # spawn("cudgel")[0].location = self
    # spawn("dirk")[0].location = self
    # spawn("iron_bar")[0].location = self
    # spawn("meat_cleaver")[0].location = self
    # spawn("short_sword")[0].location = self
    # spawn("book_of_shadows")[0].location = self
    # spawn("grand_grimoire")[0].location = self
    # spawn("mabinogian")[0].location = self

  def basetype_posthook_setup(self):
    # overriding this so we can do some post-init
    # after spawning, as BaseObject.at_first_save() applies _create_dict field values
    # *after* calling at_object_creation()
    super().basetype_posthook_setup()
    for key in self.db.for_sale_keys:
      spawn(key)[0].location = self

  def return_appearance(self, looker, **kwargs):
    table = evtable.EvTable("Item", "Cost")
    for obj in self.contents:
      table.add_row(obj.key, obj.worth)
    return f"You see a merchant, hawking their wares:\n{table}"

  def at_object_receive(self, moved_obj, source_location, **kwargs):
    # only admins can give objects to merchant to go on sale
    is_admin = (source_location and source_location.account 
      and (source_location.account.check_permstring("Developer") or source_location.account.check_permstring("Admins")))
    if not is_admin:
      moved_obj.delete()
      if source_location and hasattr(source_location, "msg"):
        source_location.msg("Sweet, merchants love free stuff.")

