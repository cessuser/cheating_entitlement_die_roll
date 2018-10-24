from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class M1Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class DiceRolling(Page):
    form_model = models.Player
    form_fields = ['report_dice', 'virtual_dice']

class DiceRollingResult(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    M1Introduction,
    DiceRolling,
    DiceRollingResult,

]
