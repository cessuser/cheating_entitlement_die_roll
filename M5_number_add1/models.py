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
    name_in_url = 'M5_number_add1'
    players_per_group = 3
    num_rounds = 30

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            nums1 = [random.randint(10, 100) for i in range(0,Constants.num_rounds)]
            nums2 = [random.randint(10, 100) for i in range(0, Constants.num_rounds)]
            for p in self.get_players():
                p.participant.vars['nums1'] = nums1
                p.participant.vars['nums2'] = nums2
                p.participant.vars['ans'] = []
                for i in range(0,Constants.num_rounds):
                    p.participant.vars['ans'].append(nums1[i] + nums2[i])
                p.participant.vars['M5_round1Pay'] = 0
                p.participant.vars['n_correct1_M5'] = 0


class Group(BaseGroup):
    def set_payoff(self):
        for p in self.get_players():
            p.payoff = 0
        player_sorted = [[p, p.participant.vars['n_correct1_M5']] for p in self.get_players()]
        player_sorted = sorted(player_sorted, key=lambda x:x[1])

        if player_sorted[0][0].roundPred == 3:
            player_sorted[0][0].payoff += 100
        if player_sorted[1][0].roundPred == 2:
            player_sorted[1][0].payoff += 100
        if player_sorted[2][0].roundPred == 1:
            player_sorted[1][0].payoff += 100

        for i in range(0, Constants.players_per_group):
            player_sorted[i][0].payoff += c(player_sorted[i][1] * 150)
            player_sorted[i][0].participant.vars['M5_round1Pay'] = player_sorted[i][0].payoff
            player_sorted[i][0].participant.vars['M5_modelPred'] = player_sorted[i][0].modelPred


class Player(BasePlayer):
    answer = models.IntegerField() # player answer
    correct = models.IntegerField() # if correct
    n_correct = models.IntegerField() # number of correct
    modelPred = models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], widget=widgets.RadioSelect)
    roundPred = models.IntegerField(choices=[1, 2, 3], widget=widgets.RadioSelect)



    def check_correct(self):
        if self.round_number == 1:
            self.participant.vars['n_correct1_M5'] = 0
        if self.answer == self.participant.vars['ans'][self.round_number-1]:
            self.correct = 1
            self.participant.vars['n_correct1_M5'] += 1
        else:
            self.correct = 0
        self.n_correct = self.participant.vars['n_correct1_M5']


