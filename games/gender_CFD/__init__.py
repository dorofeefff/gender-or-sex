from otree.api import (
    Page,
    WaitPage,
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


class Constants(BaseConstants):
    name_in_url = 'photos'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    photo_choice_1 = models.IntegerField()
    femininity_1 = models.IntegerField(
        label='Femininity',
    )
    masculinity_1 = models.IntegerField(
        label='Masculinity',
    )


# FUNCTIONS
# PAGES
class GenderCFD(Page):
    form_model = 'player'
    form_fields = ['femininity_1', 'masculinity_1']


page_sequence = [GenderCFD]
