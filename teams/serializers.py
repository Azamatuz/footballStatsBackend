from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = ''
        model = Team
        fields = ('id', 'name', 'league',)