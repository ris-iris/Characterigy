from django import forms
from django.forms import Textarea
from .models import Character, User


class ModCharForm(forms.ModelForm):
    class Meta:
        model = Character

        fields = [
            'name', 'chrclass', 'race', 'align',
            'lvl', 'exp', 'temp_hit', 'armor_class',
            'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom',
            'charisma',
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

    def clean_strength(self):
        print(self.changed_data)
        v = self.cleaned_data['strength']
        if v < 0 or v > 20:
            raise forms.ValidationError(
                "strength should be a number from 0 to 20")
        return v

    def clean_dexterity(self):
        v = self.cleaned_data['dexterity']
        if v < 0 or v > 20:
            raise forms.ValidationError(
                "dexterity should be a number from 0 to 20")
        return v

    def clean_constitution(self):
        v = self.cleaned_data['constitution']
        if v < 0 or v > 20:
            raise forms.ValidationError(
                "constitution should be a number from 0 to 20")
        return v

    def clean_intelligence(self):
        v = self.cleaned_data['intelligence']
        if v < 0 or v > 20:
            raise forms.ValidationError(
                "intelligence should be a number from 0 to 20")
        return v

    def clean_wisdom(self):
        v = self.cleaned_data['wisdom']
        if v < 0 or v > 20:
            raise forms.ValidationError(
                "wisdom should be a number from 0 to 20")
        return v

    def clean_charisma(self):
        v = self.cleaned_data['charisma']
        if v < 0 or v > 20:
            raise forms.ValidationError(
                "charisma should be a number from 0 to 20")
        return v

    def clean_silverCoins(self):
        v = self.cleaned_data['silverCoins']
        if v < 0:
            raise forms.ValidationError(
                "silver coins should be a number not lower than 0")
        return v

    def clean_copperCoins(self):
        v = self.cleaned_data['copperCoins']
        if v < 0:
            raise forms.ValidationError(
                "copper coins should be a number not lower than 0")
        return v

    def clean_goldCoins(self):
        v = self.cleaned_data['goldCoins']
        if v < 0:
            raise forms.ValidationError(
                "gold coins should be a number not lower than 0")
        return v


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SigninForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
