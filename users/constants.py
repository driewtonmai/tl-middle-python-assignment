from django.db import models


class StatusChoices(models.IntegerChoices):
    """Status choices for the Customer"""

    INACTIVE = 0, 'Неактивен'
    ACTIVE = 1, 'Активен'

    __empty__ = 'Выберите статус'


class TypeChoices(models.IntegerChoices):
    """Type choices for the Customer"""

    PRIMARY = 1, 'Первичный'
    REPEATED = 2, 'Повторный'
    EXTERNAL = 3, 'Внешний'
    INDIRECT = 4, 'Косвенный'

    __empty__ = 'Выберите тип'


class SexChoices(models.IntegerChoices):
    """Sex choices for the Customer"""

    MALE = 1, 'Мужской'
    FEMALE = 2, 'Женский'
    UNKNOWN = 3, 'Неизвестно'

