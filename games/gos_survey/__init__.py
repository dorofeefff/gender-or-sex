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


class Constants(BaseConstants):
    name_in_url = 'survey'
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
    sex = models.StringField(
        label='What sex were you assigned at birth?',
        choices=[
            ['female', 'Female'],
            ['male', 'Male'],
        ],
        widget=widgets.RadioSelect,
    )
    ethnicity = models.StringField(
        label='Which of the following best describes you?',
        choices=[
            ['asian', 'Asian or Pacific Islander'],
            ['black', 'Black or African American'],
            ['hispanic', 'Hispanic or Latino'],
            ['native', 'Native American or Alaskan Native'],
            ['white', 'White or Caucasian'],
            ['multi', 'Multiracial or Biracial'],
            ['none', 'None of the above'],
        ],
        widget=widgets.RadioSelect,
    )
    age = models.IntegerField(
        label='What is your age?',
        min=10,
        max=99,
    )
    major = models.StringField(
        label='What is your major?',
        choices=[
            ['economics', 'Economics'],
            ['humanities', 'Humanities'],
            ['engineering', 'Engineering'],
        ],
    )
    country_of_birth = models.StringField(
        label='Which country were you born in?',
        choices=[
            ['USA', 'USA'],
            ['Sweden', 'Sweden'],
            ['Russia', 'Russia'],
            ['China', 'China'],
            ['South Korea', 'South Korea'],
            ['Italy', 'Italy'],
            ['Germany', 'Germany'],
            ['Spain', 'Spain'],
        ],
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['sex', 'ethnicity', 'age', 'major', 'country_of_birth']


class FemMasc(Page):
    form_model = 'player'
    form_fields = ['femininity', 'masculinity']


page_sequence = [FemMasc, Demographics]
