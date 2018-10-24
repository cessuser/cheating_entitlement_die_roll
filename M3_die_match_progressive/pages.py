from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import random

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class RoundPred(Page):
    form_fields = ['roundPred']
    form_model = models.Player


class DiceRolling(Page):
        pass


class DiceRolling2(Page):
    def vars_for_template(self):
        self.player.roll_die()
        return{
            'roll': self.player.real_die_value
        }

class DiceRolling_pay(Page):
    pass

class DiceRolling2_pay(Page):
    def vars_for_template(self):
        self.player.roll_die2()
        return{
            'roll': self.player.real_die_value2
        }

class ModelPred(Page):
    form_model = models.Player
    form_fields = ['modelPred']

    def is_displayed(self):
        return self.round_number == 1


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):
    def vars_for_template(self):
        self.player.set_final_payoff()
        self.group.set_modelPred()

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Introduction,
    ModelPred,
    DiceRolling,
    DiceRolling2,
    DiceRolling_pay,
    DiceRolling2_pay,
    RoundPred,
    ResultsWaitPage,
    Results


]
