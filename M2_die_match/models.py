from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import xlrd
import random
author = 'Danlin Chen'

doc = """
match with previous 3 players and multiply 150 ECUs with the outcome 
"""


class Constants(BaseConstants):
    name_in_url = 'M2_die_match'
    players_per_group = 3
    num_rounds = 2
    thrown = [1,2,3,4,5,6]
    reward = [c(100),c(200),c(300),c(400),c(500),c(600)]
    file_location1 = "_static/data/170711_1143.xlsx"
    file_location2 = "_static/data/170711_1334.xlsx"
    file_location3 = "_static/data/170908_1146.xlsx"
    file_location4 = "_static/data/171006_0927.xlsx"

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            workbook1 = xlrd.open_workbook(Constants.file_location1)
            workbook2 = xlrd.open_workbook(Constants.file_location2)
            workbook3 = xlrd.open_workbook(Constants.file_location3)
            workbook4 = xlrd.open_workbook(Constants.file_location4)
            sheet1 = workbook1.sheet_by_name('170711_1143')
            sheet2 = workbook2.sheet_by_name('170711_1334')
            sheet3 = workbook3.sheet_by_name('170908_1146')
            sheet4 = workbook4.sheet_by_name('171006_0927')
            x = []
            for value in sheet1.col_values(8):
                if isinstance(value, float):
                    x.append(int(value))
            for value in sheet2.col_values(8):
                if isinstance(value, float):
                    x.append(int(value))
            for value in sheet3.col_values(8):
                if isinstance(value, float):
                    x.append(int(value))
            for value in sheet4.col_values(8):
                if isinstance(value, float):
                    x.append(int(value))
            for p in self.get_players():
                p.participant.vars['data'] = sorted(x)
                p.participant.vars['low'] = p.participant.vars['data'][0:360]
                p.participant.vars['medium'] = p.participant.vars['data'][360:720]
                p.participant.vars['high'] = p.participant.vars['data'][720:]
                p.participant.vars['dices'] = [random.randint(1,6) for i in range(0, 10)]
                p.participant.vars['dices2'] = [random.randint(1, 6) for i in range(0, 10)]
                p.participant.vars['all_m2_payoff'] = []
                p.roundPred_correct = False
                p.modelPred_correct = False


class Group(BaseGroup):
    def set_modelPred(self):
        player_pred = [[p, sum(p.participant.vars['all_m2_payoff'])] for p in self.get_players()]
        print('player predict: ', player_pred)
        player_pred = sorted(player_pred, key=lambda x: x[1])
        print('player preidct: ', player_pred)
        player_pred[0].append(1)
        player_pred[1].append(2)
        player_pred[2].append(3)

        if player_pred[0][0].modelPred == 3:
            player_pred[0][0].payoff += 100
            player_pred[0][0].modelPred_correct = True
            player_pred[0][0].participant.vars['m2_payoff'] += 100
        if player_pred[1][0].modelPred == 2:
            player_pred[1][0].payoff += 100
            player_pred[1][0].modelPred_correct = True
            player_pred[1][0].participant.vars['m2_payoff'] += 100
        if player_pred[2][0].modelPred == 1:
            player_pred[2][0].payoff += 100
            player_pred[2][0].modelPred_correct = True
            player_pred[2][0].participant.vars['m2_payoff'] += 100





    def set_payoff(self):
        dice_sort = [[p, p.real_die_value] for p in self.get_players()]
        dice_sort = sorted(dice_sort, key=lambda x:x[1])
        player_sorted = [0,0,0]
        p1_index = 0
        p2_index = 1
        p3_index = 2
        if dice_sort[0][1] == dice_sort[1][1] and random.randint(0,1): # flip with p2
            temp = p1_index
            p1_index = p2_index
            p2_index= temp
        if dice_sort[0][1] == dice_sort[2][1] and random.randint(0,1): # flip with p3
            temp = p1_index
            p1_index = p3_index
            p3_index = temp
        if dice_sort[1][1] == dice_sort[2][1] and random.randint(0,1):
            temp = p2_index
            p2_index = p3_index
            p3_index = temp
        player_sorted[p1_index] = dice_sort[0][0]
        player_sorted[p2_index] = dice_sort[1][0]
        player_sorted[p3_index] = dice_sort[2][0]

        player_sorted[0].payoff = c(150*random.sample(player_sorted[0].participant.vars['low'],1)[0])
        player_sorted[1].payoff = c(150*random.sample(player_sorted[1].participant.vars['medium'], 1)[0])
        player_sorted[2].payoff = c(150*random.sample(player_sorted[2].participant.vars['high'], 1)[0])

        player_sorted[0].payoff += player_sorted[0].real_die_value2 * 100
        player_sorted[1].payoff += player_sorted[0].real_die_value2 * 100
        player_sorted[2].payoff += player_sorted[0].real_die_value2 * 100

        if player_sorted[0].roundPred == 3:
            player_sorted[0].payoff += 100
            player_sorted[0].roundPred_correct = True
        if player_sorted[1].roundPred == 2:
            player_sorted[1].payoff += 100
            player_sorted[1].roundPred_correct = True
        if player_sorted[2].roundPred == 1:
            player_sorted[2].payoff += 100
            player_sorted[2].roundPred_correct = True

        player_sorted[0].participant.vars['all_m2_payoff'].append(player_sorted[0].payoff)
        player_sorted[1].participant.vars['all_m2_payoff'].append(player_sorted[1].payoff)
        player_sorted[2].participant.vars['all_m2_payoff'].append(player_sorted[2].payoff)

        print([[p, p.payoff, p.roundPred, p.real_die_value] for p in player_sorted])


class Player(BasePlayer):
    real_die_value = models.IntegerField()
    real_die_value2 = models.IntegerField()
    modelPred = models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], widget=widgets.RadioSelect)
    roundPred = models.IntegerField(choices=[1, 2, 3], widget=widgets.RadioSelect)
    final_payoff = models.CurrencyField()
    chosen_round = models.IntegerField()
    roundPred_correct = models.BooleanField()
    modelPred_correct = models.BooleanField()


    def roll_die(self):
        self.real_die_value = self.participant.vars['dices'][self.round_number-1]
        print(self.real_die_value)

    def roll_die2(self):
        self.real_die_value2 = self.participant.vars['dices2'][self.round_number-1]
        print(self.real_die_value2)

    def set_final_payoff(self):
        self.chosen_round = random.randint(1, Constants.num_rounds)
        self.final_payoff = self.participant.vars['all_m2_payoff'][self.chosen_round-1]
        self.participant.vars['chosen_round_m2'] = self.chosen_round