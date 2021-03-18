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
    femininity_1 = models.IntegerField(
        label='Femininity',
    )
    masculinity_1 = models.IntegerField(
        label='Masculinity',
    )
    ph_1 = models.IntegerField()
    ph_2 = models.IntegerField()


# FUNCTIONS
# PAGES
class GenderCFD(Page):
    form_model = "player"
    form_fields = ["femininity_1", "masculinity_1"]

    # Generate indices of photos to show to this subject
    def vars_for_template(self):
        photo_1, photo_2 = random.sample(range(1, 6), 2)
        self.ph_1 = photo_1
        self.ph_2 = photo_2
        return {
            "photo_1": photo_1,
            "photo_2": photo_2,
        }


page_sequence = [GenderCFD]
