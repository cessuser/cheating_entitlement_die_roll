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
    name_in_url = 'LastModel'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_payoff(self):
        player_lst = [[p, p.participant.vars['M5_round1Pay'] + p.participant.vars['M5_round2Pay'] + p.participant.vars['M5_round3Pay']
                       + p.participant.vars['M5_round4Pay'] + p.participant.vars['M5_round5Pay']] for p in self.get_players()]
        player_lst = sorted(player_lst, key=lambda x: x[1])
        num_players = len(self.get_players())
        print('player lst', player_lst)
        for i in range(0,len(self.get_players())):
            cur_player = cur_player
            cur_player.payoff = 0
            payoffs = [cur_player.participant.vars['M5_round1Pay'],
                       cur_player.participant.vars['M5_round2Pay'],
                       cur_player.participant.vars['M5_round3Pay'],
                       cur_player.participant.vars['M5_round4Pay'],
                       cur_player.participant.vars['M5_round5Pay']]

            print('player id: ', i, ' ', payoffs)
            cur_player.chosen = random.randint(0,len(payoffs)-1)
            cur_player.payoff = payoffs[cur_player.chosen]
            if cur_player.participant.vars['M5_modelPred'] == 3 and i < num_players/3:
                cur_player.payoff += 100
            if cur_player.participant.vars['M5_modelPred'] == 2 and num_players/3 <= i < num_players*2/3:
                cur_player.payoff += 100
            if cur_player.participant.vars['M5_modelPred'] == 1 and num_players*2/3 <= i:
                cur_player.payoff += 100

            cur_player.participant.vars['M5_payoff'] = cur_player.payoff

    def set_final_payoff(self):
        for p in self.get_players():
            p.payoff = p.participant.vars['M1_payoff'] + p.participant.vars['m2_payoff'] + p.participant.vars['m3_payoff'] \
                       + p.participant.vars['M4_payoff'] + p.participant.vars['M5_payoff']

class Player(BasePlayer):
    chosen = models.IntegerField()