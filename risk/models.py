from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
Risk game
"""


class Constants(BaseConstants):
    name_in_url = 'risk'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'risk/Instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['choice'] = int(random.choice([1, 2, 3, 4, 5, 6, 7, 8]))
            p.participant.vars['selected_game'] = int(random.choice([1, 2, 3, 4, 5, 6]))


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    d1 = models.PositiveIntegerField(
        choices=[[1, 'A: get 75ECU directly'],
                 [2, 'B: get 0ECU if the dice shows 1, 2 or 3; If Dice shows 4, 5 or 6 then 200ECU.']],
        verbose_name='This is decision 1',
        widget=widgets.RadioSelect()
    )

    d2 = models.PositiveIntegerField(
        choices=[[1, 'A: get 75ECU directly'],
                 [2, 'B: get 0ECU if the dice shows 1, 2 or 3; If Dice shows 4, 5 or 6 then 185ECU.']],
        verbose_name='This is decision 2',
        widget=widgets.RadioSelect()
    )

    d3 = models.PositiveIntegerField(
        choices=[[1, 'A: get 75ECU directly'],
                 [2, 'B: get 0ECU if the dice shows 1, 2 or 3; If Dice shows 4, 5 or 6 then 170ECU.']],
        verbose_name='This is decision 3',
        widget=widgets.RadioSelect()
    )

    d4 = models.PositiveIntegerField(
        choices=[[1, 'A: get 75ECU directly'],
                 [2, 'B: get 0ECU if the dice shows 1, 2 or 3; If Dice shows 4, 5 or 6 then 155ECU.']],
        verbose_name='This is decision 4',
        widget=widgets.RadioSelect()
    )

    d5 = models.PositiveIntegerField(
        choices=[[1, 'A: get 75ECU directly'],
                 [2, 'B: get 0ECU if the dice shows 1, 2 or 3; If Dice shows 4, 5 or 6 then 140ECU.']],
        verbose_name='This is decision 5',
        widget=widgets.RadioSelect()
    )

    d6 = models.PositiveIntegerField(
        choices=[[1, 'A: get 75ECU directly'],
                 [2, 'B: get 0ECU if the dice shows 1, 2 or 3; If Dice shows 4, 5 or 6 then 125ECU.']],
        verbose_name='This is decision 6',
        widget=widgets.RadioSelect()
    )

    d7 = models.PositiveIntegerField(
        choices=[[1, 'A: get 75ECU directly'],
                 [2, 'B: get 0ECU if the dice shows 1, 2 or 3; If Dice shows 4, 5 or 6 then 110ECU.']],
        verbose_name='This is decision 7',
        widget=widgets.RadioSelect()
    )

    d8 = models.PositiveIntegerField(
        choices=[[1,'A: get 75ECU directly'],
                 [2, 'B: get 0ECU if the dice shows 1, 2 or 3; If Dice shows 4, 5 or 6 then 95ECU.']],
        verbose_name='This is decision 8',
        widget=widgets.RadioSelect()
    )

    risk_choice1 = models.PositiveIntegerField()
    risk_choice2 = models.PositiveIntegerField()
    risk_choice3 = models.PositiveIntegerField()
    risk_choice4 = models.PositiveIntegerField()
    risk_choice5 = models.PositiveIntegerField()
    risk_choice6 = models.PositiveIntegerField()
    risk_choice7 = models.PositiveIntegerField()
    risk_choice8 = models.PositiveIntegerField()
    diceFinal = models.PositiveIntegerField()
    choice_selected = models.PositiveIntegerField()

    def set_payoffs(self):
        if self.participant.vars['choice'] == 1:
            self.payoff = self.risk_choice1
        elif self.participant.vars['choice'] == 2:
           self.payoff = self.risk_choice2
        elif self.participant.vars['choice'] == 3:
            self.payoff = self.risk_choice3
        elif self.participant.vars['choice'] == 4:
            self.payoff = self.risk_choice4
        elif self.participant.vars['choice'] == 5:
            self.payoff = self.risk_choice5
        elif self.participant.vars['choice'] == 6:
            self.payoff = self.risk_choice6
        elif self.participant.vars['choice'] == 7:
            self.payoff = self.risk_choice7
        else:
            self.payoff = self.risk_choice8

