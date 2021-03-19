from otree.api import *
import random


class Constants(BaseConstants):
    name_in_url = 'photos'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    femininity_1 = models.IntegerField(
        label='Femininity',
    )
    masculinity_1 = models.IntegerField(
        label='Masculinity',
    )
    photo_this_round = models.IntegerField()


# FUNCTIONS

# Choose photos that will be shown to the subjects
def creating_session(subsession):
    # In the first round, create lists of photos for all rounds
    if subsession.round_number == 1:
        for player in subsession.get_players():
            player.participant.photo_ids_global = random.sample(range(1, 7), k=3)
            player.photo_this_round = player.participant.photo_ids_global[0]
    # In all other rounds, choose from the list created in round 1
    else:
        for player in subsession.get_players():
            player.photo_this_round = player.participant.photo_ids_global[subsession.round_number-1]


# PAGES
class GenderCFD(Page):
    form_model = "player"
    form_fields = ["femininity_1", "masculinity_1"]


page_sequence = [GenderCFD]
