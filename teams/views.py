from urllib import request
from django.forms import model_to_dict
from rest_framework.views import APIView, Response, Request, status
from .models import Team
from utils import *
from exceptions import *


class Teamview(APIView):
    def post(self, request: Request) -> Response:
        try:
            data_processing(request.data)
        except NegativeTitlesError as err:
            dict_error = {"error": f'{err.message}'}
            return Response(dict_error, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as err:
            dict_error = {"error": f'{err.message}'}
            return Response(dict_error, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as err:
            dict_error = {"error": f'{err.message}'}
            return Response(dict_error, status.HTTP_400_BAD_REQUEST)      
        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)
        team_id = (team_dict["id"])
        team_str = Team.__repr__(team)    
        return Response(team_dict, status.HTTP_201_CREATED)
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        teams_dict = []
        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)
        return Response(teams_dict)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            dict_error = {"message": "Team not found"}
            return Response(dict_error, status.HTTP_404_NOT_FOUND)
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)
    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            dict_error = {"message": "Team not found"}
            return Response(dict_error, status.HTTP_404_NOT_FOUND)
        for key, value in request.data.items():
            setattr(team, key, value)
        team.save()
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)
    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            dict_error = {"message": "Team not found"}
            return Response(dict_error, status.HTTP_404_NOT_FOUND)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
