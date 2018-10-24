from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

import random


class Introduction(Page):
    """Description of the game: How to play and returns expected"""

    def is_displayed(self):
        return Constants.num_rounds == 1



class D1(Page):
    form_model = 'player'
    form_fields = ['d1']

    def before_next_page(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        if self.player.d1 == 1:
            self.player.risk_choice1 = 20
        else:
            if dice <= 3:
                self.player.risk_choice1 = 0
            else:
                self.player.risk_choice1 = 56


class D2(Page):
    form_model = 'player'
    form_fields = ['d2']

    def before_next_page(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        if self.player.d2 == 1:
            self.player.risk_choice2 = 20
        else:
            if dice <= 3:
                self.player.risk_choice2 = 0
            else:
                self.player.risk_choice2 = 52


class D3(Page):
    form_model = 'player'
    form_fields = ['d3']

    def before_next_page(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        if self.player.d3 == 1:
            self.player.risk_choice3 = 20
        else:
            if dice <= 3:
                self.player.risk_choice3 = 0
            else:
                self.player.risk_choice3 = 48


class D4(Page):
    form_model = 'player'
    form_fields = ['d4']

    def before_next_page(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        if self.player.d4 == 1:
            self.player.risk_choice4 = 20
        else:
            if dice <= 3:
                self.player.risk_choice4 = 0
            else:
                self.player.risk_choice4 = 44


class D5(Page):
    form_model = 'player'
    form_fields = ['d5']

    def before_next_page(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        if self.player.d5 == 1:
            self.player.risk_choice5 = 20
        else:
            if dice <= 3:
                self.player.risk_choice5 = 0
            else:
                self.player.risk_choice5 = 40


class D6(Page):
    form_model = 'player'
    form_fields = ['d6']

    def before_next_page(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        if self.player.d6 == 1:
            self.player.risk_choice6 = 20
        else:
            if dice <= 3:
                self.player.risk_choice6 = 0
            else:
                self.player.risk_choice6 = 36


class D7(Page):
    form_model = 'player'
    form_fields = ['d7']

    def before_next_page(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        if self.player.d7 == 1:
            self.player.risk_choice7 = 20
        else:
            if dice <= 3:
                self.player.risk_choice7 = 0
            else:
                self.player.risk_choice7 = 32


class D8(Page):
    form_model = 'player'
    form_fields = ['d8']

    def before_next_page(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        if self.player.d8 == 1:
            self.player.risk_choice8 = 20
        else:
            if dice <= 3:
                self.player.risk_choice8 = 0
            else:
                self.player.risk_choice8 = 28

        self.player.choice_selected = self.participant.vars['choice']
        self.player.set_payoffs()
        self.participant.vars['payoff_risk'] = self.player.payoff


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    """Players payoff: How much each has earned"""

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'final': self.participant.vars['choice'],
            'payoff': self.player.payoff,
        }


page_sequence = [
    Introduction,
    D1,
    D2,
    D3,
    D4,
    D5,
    D6,
    D7,
    D8,
    ResultsWaitPage,
    Results,
]
