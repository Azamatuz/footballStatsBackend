from django.urls import path
from .views import ListTeam, DetailTeam

urlpatterns = [
    path('<int:pk>/', DetailTeam.as_view()),
    path('', ListTeam.as_view())
]
