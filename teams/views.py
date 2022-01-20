from rest_framework import generics
from .models import Team
from .serializers import TeamSerializer

class ListTeam(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
class DetailTeam(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
