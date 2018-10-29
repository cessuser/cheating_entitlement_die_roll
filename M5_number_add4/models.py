from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'M5_number_add4'
    players_per_group = 3
    num_rounds = 30

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            nums1 = [48, 93, 37, 49, 80, 49, 41, 95, 27, 34, 28, 27, 10, 80, 89, 86, 69, 17, 56, 77, 62, 36, 19, 90, 38, 63, 79, 95, 29, 92]
            nums2 = [30, 54, 79, 95, 12, 94, 55, 97, 66, 91, 47, 78, 35, 68, 47, 26, 76, 69, 52, 59, 43, 74, 67, 87, 61, 57, 39, 58, 83, 73]
            for p in self.get_players():
                p.participant.vars['nums1'] = nums1
                p.participant.vars['nums2'] = nums2
                p.participant.vars['ans'] = []
                for i in range(0,Constants.num_rounds):
                    p.participant.vars['ans'].append(nums1[i] + nums2[i])
                p.participant.vars['M5_round4Pay'] = 0
                p.participant.vars['n_correct4_M5'] = 0


class Group(BaseGroup):
    def set_payoff(self):
        player_sorted = [[p, p.participant.vars['n_correct4_M5'], p.roundPred] for p in self.get_players()]
        player_sorted = sorted(player_sorted, key=lambda x:x[1])

        for p in self.get_players():
            p.payoff = 0
        if player_sorted[0][0].roundPred == 3:
            player_sorted[0][0].payoff += 100
        if player_sorted[1][0].roundPred == 2:
            player_sorted[1][0].payoff += 100
        if player_sorted[2][0].roundPred == 1:
            player_sorted[2][0].payoff += 100

        for i in range(0, Constants.players_per_group):
            player_sorted[i][0].payoff += c(player_sorted[i][1] * 150)
            player_sorted[i][0].participant.vars['M5_round4Pay'] = player_sorted[i][0].payoff


class Player(BasePlayer):
    answer = models.IntegerField() # player answer
    correct = models.IntegerField() # if correct
    n_correct = models.IntegerField() # number of correct
    roundPred = models.IntegerField(choices=[1, 2, 3], widget=widgets.RadioSelect)


    def check_correct(self):
        if self.round_number == 1:
            self.participant.vars['n_correct4_M5'] = 0
        if self.answer == self.participant.vars['ans'][self.round_number-1]:
            self.correct = 1
            self.participant.vars['n_correct4_M5'] += 1
        else:
            self.correct = 0
        self.n_correct = self.participant.vars['n_correct4_M5']


