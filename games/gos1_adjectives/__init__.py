from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'part1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    femininity = models.LongStringField(
        label='Write down adjectives associated with femininity here. Separate different adjectives by a comma.',
    )
    masculinity = models.LongStringField(
        label='Write down adjectives associated with masculinity here. Separate different adjectives by a comma.',
    )


# FUNCTIONS
# PAGES


class FemMasc(Page):
    form_model = 'player'
    form_fields = ['femininity', 'masculinity']


page_sequence = [FemMasc]
