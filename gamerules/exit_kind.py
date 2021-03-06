from enum import IntEnum


class ExitKind(IntEnum):
  NO_EXIT = 0
  OPEN = 1
  OBJECT_REQUIRED = 2
  OBJECT_FORBIDDEN = 3
  RANDOM_FAIL = 4
  POTENTIAL_EXIT = 5
  ONLY_EXISTS_WITH_OBJECT = 6
  TIMED_OPEN_CLOSE = 7
  PASSWORDED = 8