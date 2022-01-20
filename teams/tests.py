from django.test import TestCase
from .models import Team

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Team.objects.create(name='first team', league='a league here')
    
    def test_name_content(self):
        team = Team.objects.get(id=1)
        expected_object_name = f'{team.name}'
        self.assertEqual(expected_object_name, 'first team')
    
    def test_league_content(self):
        team = Team.objects.get(id=1)
        expected_object_name = f'{team.league}'
        self.assertEqual(expected_object_name, 'a league here')