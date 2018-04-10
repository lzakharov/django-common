from enum import Enum


class ChoiceEnum(Enum):
    """Allows to use Enum as choices for fields."""
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)
