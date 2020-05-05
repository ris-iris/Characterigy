from django import forms
from django.forms import Textarea
from .models import Character, User


class ModCharForm(forms.ModelForm):
    class Meta:
        model = Character

        fields = [
            'name', 'chrclass', 'race', 'align',
            'lvl', 'exp', 'temp_hit', 'armor_class',
            'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
            'acrobatic',
            'animal_handling',
            'arcana',
            'athletics',
            'deception',
            'history',
            'insight',
            'intimidation',
            'investigation',
            'medicine',
            'nature',
            'perception',
            'performance',
            'persuasion',
            'religion',
            'sleight_of_hand',
            'stealth',
            'survival',
            'equipment',
            'weapon1',
            'weapon2',
            'weapon3',
            'damage1',
            'damage2',
            'damage3',
            'damagetype1',
            'damagetype2',
            'damagetype3',
            'additional',
            'goldCoins',
            'silverCoins',
            'copperCoins',
            'traits',
            'ideals',
            'bonds',
            'flaws',
            'organizations',
            'backstory',
            'treasure'
        ]
        widgets = {
            'additional': Textarea,
            'equipment': Textarea,
            'traits': Textarea,
            'ideals': Textarea,
            'bonds': Textarea,
            'flaws': Textarea,
            'organizations': Textarea,
            'backstory': Textarea,
            'treasure': Textarea,
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SigninForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
