import math

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse

from .models import User, Character
from .forms import LoginForm, ModCharForm, SigninForm


def signin(request):
    if request.method == 'POST':
        user_form = SigninForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return redirect('login')
    else:
        user_form = SigninForm()
    return render(request, 'mainapp/signin.html', {'form': user_form})


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('user', user.id)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'mainapp/login.html', {'form': form})


def user(request, user_id):
    temp_user = User.objects.get(pk=user_id)
    template = loader.get_template('mainapp/user.html')
    context = {
        'user': temp_user,
        'characters_list': temp_user.character_set.all(),
    }
    return HttpResponse(template.render(context, request))


def chracter_data_pack(character_id):
    temp_character = Character.objects.get(pk=character_id)

    context = {
        'character': temp_character,
        'class_special_features': eval(
            temp_character.chrclass.special_features),
        'race_special_features': eval(
            temp_character.race.special_features),
        'hits': eval(temp_character.chrclass.hits),
        'saving_throw': eval(temp_character.chrclass.saving_throwth),
        'mod': {'str': math.floor((temp_character.strength - 10) / 2),
                'dex': math.floor((temp_character.dexterity - 10) / 2),
                'con': math.floor((temp_character.constitution - 10) / 2),
                'int': math.floor((temp_character.intelligence - 10) / 2),
                'wis': math.floor((temp_character.wisdom - 10) / 2),
                'char': math.floor((temp_character.charisma - 10) / 2)},
        'armor': eval(temp_character.chrclass.props_and_langs)['armor'] + ', ' +
                 eval(temp_character.race.props_and_langs)['armor'],
        'weapon': eval(temp_character.chrclass.props_and_langs)[
                      'weapon'] + ', ' +
                  eval(temp_character.race.props_and_langs)['weapon'],
        'tools': eval(temp_character.chrclass.props_and_langs)['tools'] + ', ' +
                 eval(temp_character.race.props_and_langs)['tools'],
        'langs': eval(temp_character.chrclass.props_and_langs)['langs'] + ', ' +
                 eval(temp_character.race.props_and_langs)['langs'],
    }

    return context


def character(request, user_id, character_id):
    template = loader.get_template('mainapp/sheet.html')
    context = chracter_data_pack(character_id)
    return HttpResponse(template.render(context, request))


def create_character(request, user_id):
    template = loader.get_template('mainapp/create.html')
    form = ModCharForm(request.POST or None)
    if form.is_valid():
        temp_character = form.save(commit=False)
        temp_character.player = User.objects.get(pk=user_id)
        temp_character.save()
        return redirect('user', user_id)
    else:
        print(form.errors)

    context = {'player': User.objects.get(pk=user_id), 'form': form}
    return HttpResponse(template.render(context, request))
