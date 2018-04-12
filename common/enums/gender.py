from src.apps.common.enums import ChoiceEnum
from django.utils.translation import ugettext_lazy as _


class Gender(ChoiceEnum):
    M = _('Мужчина')
    F = _('Женщина')
