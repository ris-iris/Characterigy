from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .forms import ModCharForm
from .models import ChrClass, Race, Character, User


class CharFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ChrClass.objects.create(
            name='1',
            hits='1',
            saving_throwth='1',
            special_features='1',
            props_and_langs='1',
            in_growh='1'
        )
        Race.objects.create(
            name='1',
            characteristic_increase='1',
            size='S',
            special_features='1',
            props_and_langs='1',
            speed='1'
        )
        cls.form_data1 = {'name': 'name1',
                          'chrclass': ChrClass.objects.get(pk=1),
                          'race': ChrClass.objects.get(pk=1),
                          'align': 'CG',
                          'lvl': 1, 'exp': 0, 'temp_hit': 0, 'armor_class': 0,
                          'strength': 1, 'dexterity': 2, 'constitution': 3,
                          'intelligence': 4,
                          'wisdom': 5,
                          'charisma': 6, 'goldCoins': 1,
                          'silverCoins': 1,
                          'copperCoins': 1}
        cls.form_data2 = {'name': 'name2',
                          'chrclass': ChrClass.objects.get(pk=1),
                          'race': ChrClass.objects.get(pk=1),
                          'align': 'CG',
                          'lvl': 2, 'exp': 0, 'temp_hit': 0, 'armor_class': 0,
                          'strength': 2, 'dexterity': 2, 'constitution': 3,
                          'intelligence': 4,
                          'wisdom': 5,
                          'charisma': 6, 'goldCoins': 2,
                          'silverCoins': 2,
                          'copperCoins': 2}

    def test_correct_strength(self):
        print(self.form_data1)
        self.form_data1['strength'] = 10
        self.form_data2['strength'] = -10
        form1 = ModCharForm(data=self.form_data1)
        form2 = ModCharForm(data=self.form_data2)
        self.assertFalse(form2.is_valid())
        self.assertTrue(form1.is_valid())
        self.form_data2['strength'] = 10

    def test_correct_dexterity(self):
        self.form_data1['dexterity'] = 10
        self.form_data2['dexterity'] = -10
        form1 = ModCharForm(data=self.form_data1)
        form2 = ModCharForm(data=self.form_data2)
        self.assertFalse(form2.is_valid())
        self.assertTrue(form1.is_valid())
        self.form_data2['dexterity'] = 10

    def test_correct_constitution(self):
        self.form_data1['constitution'] = 10
        self.form_data2['constitution'] = -10
        form1 = ModCharForm(data=self.form_data1)
        form2 = ModCharForm(data=self.form_data2)
        self.assertFalse(form2.is_valid())
        self.assertTrue(form1.is_valid())
        self.form_data2['constitution'] = 10

    def test_correct_intelligence(self):
        self.form_data1['intelligence'] = 10
        self.form_data2['intelligence'] = -10
        form1 = ModCharForm(data=self.form_data1)
        form2 = ModCharForm(data=self.form_data2)
        self.assertFalse(form2.is_valid())
        self.assertTrue(form1.is_valid())
        self.form_data2['intelligence'] = 10

    def test_correct_wisdom(self):
        self.form_data1['wisdom'] = 10
        self.form_data2['wisdom'] = -10
        form1 = ModCharForm(data=self.form_data1)
        form2 = ModCharForm(data=self.form_data2)
        self.assertFalse(form2.is_valid())
        self.assertTrue(form1.is_valid())
        self.form_data2['wisdom'] = 10

    def test_correct_charisma(self):
        self.form_data1['charisma'] = 10
        self.form_data2['charisma'] = -10
        form1 = ModCharForm(data=self.form_data1)
        form2 = ModCharForm(data=self.form_data2)
        self.assertFalse(form2.is_valid())
        self.assertTrue(form1.is_valid())
        self.form_data2['charisma'] = 10

    def test_correct_goldCoins(self):
        self.form_data1['goldCoins'] = 10
        self.form_data2['goldCoins'] = -10
        form1 = ModCharForm(data=self.form_data1)
        form2 = ModCharForm(data=self.form_data2)
        self.assertFalse(form2.is_valid())
        self.assertTrue(form1.is_valid())
        self.form_data2['goldCoins'] = 10

    def test_correct_silverCoins(self):
        self.form_data1['silverCoins'] = 10
        self.form_data2['silverCoins'] = -10
        form1 = ModCharForm(data=self.form_data1)
        form2 = ModCharForm(data=self.form_data2)
        self.assertFalse(form2.is_valid())
        self.assertTrue(form1.is_valid())
        self.form_data2['silverCoins'] = 10

    def test_correct_copperCoins(self):
        self.form_data1['copperCoins'] = 10
        self.form_data2['copperCoins'] = -10
        form1 = ModCharForm(data=self.form_data1)
        form2 = ModCharForm(data=self.form_data2)
        self.assertFalse(form2.is_valid())
        self.assertTrue(form1.is_valid())
        self.form_data2['copperCoins'] = 10


class UserTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1',
                                              password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2',
                                              password='12345')
        test_user2.save()

        ChrClass.objects.create(
            name='1',
            hits='1',
            saving_throwth='1',
            special_features='1',
            props_and_langs='1',
            in_growh='1'
        )
        Race.objects.create(
            name='1',
            characteristic_increase='1',
            size='S',
            special_features='1',
            props_and_langs='1',
            speed='1'
        )
        character1 = Character.objects.create(
            name='name1',
            player=User.objects.get(username='testuser1'),
            chrclass=ChrClass.objects.get(pk=1),
            race=Race.objects.get(pk=1),
            align='CG',
            lvl=1, exp=0, temp_hit=0, armor_class=0,
            strength=1, dexterity=2, constitution=3,
            intelligence=4,
            wisdom=5,
            charisma=6, goldCoins=1,
            silverCoins=1,
            copperCoins=1
        )
        character2 = Character.objects.create(
            name='name2',
            player=User.objects.get(username='testuser1'),
            chrclass=ChrClass.objects.get(pk=1),
            race=Race.objects.get(pk=1),
            align='CG',
            lvl=1, exp=0, temp_hit=0, armor_class=0,
            strength=1, dexterity=2, constitution=3,
            intelligence=4,
            wisdom=5,
            charisma=6, goldCoins=1,
            silverCoins=1,
            copperCoins=1
        )

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse_lazy('user', args=[
            User.objects.get(username='testuser1').id]))
        self.assertRedirects(resp, '/login?next=/3/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse_lazy('user', args=[
            User.objects.get(username='testuser1').id]))
        self.assertEqual(str(resp.context['user']), 'testuser1')
        self.assertEqual(resp.status_code, 200)
