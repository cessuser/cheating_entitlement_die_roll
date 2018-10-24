from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Danlin Chen'

doc = """
Die Game and dictator 
"""


class Constants(BaseConstants):
    name_in_url = 'M1_die_game'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    report_dice = models.IntegerField(min=1, max=6,
                                      verbose_name= 'Please input the die number')
    virtual_dice = models.StringField(verbose_name='given of the system', blank=True)
