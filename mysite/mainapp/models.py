from django.db import models
from django.contrib.auth.models import User


class ChrClass(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    # some special format
    hits = models.CharField(max_length=3000)
    saving_throwth = models.CharField(max_length=3000)
    special_features = models.CharField(max_length=3000)
    props_and_langs = models.CharField(max_length=3000)
    in_growh = models.CharField(max_length=3000)

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    # some special format
    characteristic_increase = models.CharField(max_length=3000)
    special_features = models.CharField(max_length=3000)
    props_and_langs = models.CharField(max_length=3000)

    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    size = models.CharField(max_length=1, choices=SIZES)
    speed = models.IntegerField()

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=30)
    chrclass = models.ForeignKey(ChrClass, on_delete=models.DO_NOTHING,)
    player = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    race = models.ForeignKey(Race, on_delete=models.DO_NOTHING,)
    ALIGN = (
        ('LG', 'lawful good'),
        ('NG', 'neutral good'),
        ('CG', 'chaotic good'),
        ('LN', 'lawful neutral'),
        ('NN', 'truly neutral(boring)'),
        ('CN', 'chaotic neutral'),
        ('LE', 'lawful evil'),
        ('NE', 'neutral evil'),
        ('CE', 'chaotic evil'),
    )
    align = models.CharField(max_length=2, choices=ALIGN)

    lvl = models.IntegerField()
    exp = models.IntegerField()
    temp_hit = models.IntegerField()
    armor_class = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    # to mark if it's chosen
    acrobatic = models.BooleanField(default=False)
    animal_handling = models.BooleanField(default=False)
    arcana = models.BooleanField(default=False)
    athletics = models.BooleanField(default=False)
    deception = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    insight = models.BooleanField(default=False)
    intimidation = models.BooleanField(default=False)
    investigation = models.BooleanField(default=False)
    medicine = models.BooleanField(default=False)
    nature = models.BooleanField(default=False)
    perception = models.BooleanField(default=False)
    performance = models.BooleanField(default=False)
    persuasion = models.BooleanField(default=False)
    religion = models.BooleanField(default=False)
    sleight_of_hand = models.BooleanField(default=False)
    stealth = models.BooleanField(default=False)
    survival = models.BooleanField(default=False)

    # it should show the "list" in html
    equipment = models.CharField(max_length=3000, blank=True)

    weapon1 = models.CharField(max_length=30, blank=True)
    weapon2 = models.CharField(max_length=30, blank=True)
    weapon3 = models.CharField(max_length=30, blank=True)
    damage1 = models.CharField(max_length=5, blank=True)
    damage2 = models.CharField(max_length=5, blank=True)
    damage3 = models.CharField(max_length=5, blank=True)
    damagetype1 = models.CharField(max_length=30, blank=True)
    damagetype2 = models.CharField(max_length=30, blank=True)
    damagetype3 = models.CharField(max_length=30, blank=True)
    additional = models.CharField(max_length=3000, blank=True)

    goldCoins = models.IntegerField()
    silverCoins = models.IntegerField()
    copperCoins = models.IntegerField()

    # just strings
    traits = models.CharField(max_length=3000, blank=True)
    ideals = models.CharField(max_length=3000, blank=True)
    bonds = models.CharField(max_length=3000, blank=True)
    flaws = models.CharField(max_length=3000, blank=True)

    organizations = models.CharField(max_length=3000, blank=True)
    backstory = models.CharField(max_length=3000, blank=True)
    additional = models.CharField(max_length=3000, blank=True)
    treasure = models.CharField(max_length=3000, blank=True)

    def __str__(self):
        return self.name
