from django.urls import path
from .views import TeamDetailView, Teamview

urlpatterns = [
    path('teams/', Teamview.as_view()),
    path('teams/<int:team_id>/', TeamDetailView.as_view())
]
