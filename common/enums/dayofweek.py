from src.apps.common.enums import ChoiceEnum
from django.utils.translation import ugettext_lazy as _


class DayOfWeek(ChoiceEnum):
    MONDAY = _('Понедельник')
    TUESDAY = _('Вторник')
    WEDNESDAY = _('Среда')
    THURSDAY = _('Четверг')
    FRIDAY = _('Пятница')
    SATURDAY = _('Суббота')
    SUNDAY = _('Воскресенье')
