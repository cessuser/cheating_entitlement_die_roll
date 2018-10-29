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
    def vars_for_template(self):
        return {
            'round_num': self.round_number
        }


class DiceRolling2(Page):
    def vars_for_template(self):
        self.player.roll_die()
        return{
            'roll': self.player.real_die_value,
            'round_num': self.round_number
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


class RealDiceRolling(Page):
    form_fields = ['dice_value']
    form_model = models.Player

    def vars_for_template(self):
        return {
            'round_num': self.round_number
        }

page_sequence = [
    Introduction,
    ModelPred,
    RoundPred,
    DiceRolling,
    DiceRolling2,
    RealDiceRolling,
    ResultsWaitPage,
    Results


]
