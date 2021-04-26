from otree.api import *
import random
from os import listdir


class Constants(BaseConstants):
    name_in_url = 'part2'
    players_per_group = None
    num_rounds = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    femininity_value = models.IntegerField(
        label='Femininity',
    )
    masculinity_value = models.IntegerField(
        label='Masculinity',
    )
    photo_this_round = models.StringField()


# FUNCTIONS

# Choose photos that will be shown to the subjects
def creating_session(subsession):
    # In the first round, create lists of photos for all rounds
    if subsession.round_number == 1:
        for player in subsession.get_players():
            player.participant.photo_ids_global = random.sample([f for f in listdir("_static/CFD")], k=Constants.num_rounds)
#            player.participant.photo_ids_global = random.sample(range(1,7), k=3)
            player.photo_this_round = player.participant.photo_ids_global[0]
    # In all other rounds, choose from the list created in round 1
    else:
        for player in subsession.get_players():
            player.photo_this_round = player.participant.photo_ids_global[subsession.round_number-1]


# PAGES
class GenderCFD(Page):
    form_model = "player"
    form_fields = ["femininity_value", "masculinity_value"]


page_sequence = [GenderCFD]
