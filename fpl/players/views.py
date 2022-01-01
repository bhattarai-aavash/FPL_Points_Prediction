from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Players, Team
from django.views.generic import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
#import requests
#import csv
#import pandas as pd
# Create your views here.

# https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2021-22/gws/merged_gw.csv


class IndexView(View):
    def get(self, request, team_id):
        # gk = request.POST.get('goalkeeper')
        # def1 = request.POST.get('defender1')
        n_user = request.user
        team = Team.objects.filter(user__username=n_user)
        player = Players.objects.all()
        # print(team[0].id)
        '''
        res = pd.read_csv(
            'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2021-22/gws/merged_gw.csv')
        for NAME, TEAM, POS in zip(res.name, res.team, res.position):
            print(NAME+"\n")
            print(TEAM+"\n")
            print(POS+"\n")
            '''
        context = {
            'team': team,
            'player': player,
            'team_id': team_id,
            # 'response': response,
            # 'forward1': forward1,
            # 'forward2': forward2,
        }
        return render(request, 'players/index.html', context)

    def post(self, request, team_id):
        team = Team.objects.get(pk=team_id)
        forward1 = request.POST.get('forward1')
        forward2 = request.POST.get('forward2')
        defender1 = request.POST.get('defender1')
        defender2 = request.POST.get('defender2')
        defender3 = request.POST.get('defender3')
        defender4 = request.POST.get('defender4')
        midfielder1 = request.POST.get('mid-fielder1')
        midfielder2 = request.POST.get('mid-fielder2')
        midfielder3 = request.POST.get('mid-fielder3')
        midfielder4 = request.POST.get('mid-fielder4')
        goalkeeper1 = request.POST.get('goalkeeper1')
        goalkeeper2 = request.POST.get('goalkeeper2')
        if forward1 == forward2 or midfielder1 == midfielder2 or midfielder3 == midfielder4 or midfielder1 == midfielder3 or midfielder1 == midfielder4 or midfielder2 == midfielder3 or midfielder2 == midfielder4:
            respond = "You cannot choose the same forwards. Choose the another one."
        elif defender1 == defender2 or defender1 == defender3 or defender1 == defender4 or defender2 == defender3 or defender2 == defender4 or defender3 == defender4:
            respond = "You cannot choose the same defenders. Choose the another one."
        elif goalkeeper1 == goalkeeper2:
            respond = "You cannot choose the same goalkeepers. Choose the another one."
        else:
            respond = ''
            ''' 
            forwards = team.players.filter(type="FWD")
            defenders = team.players.filter(type="DEF")
            midfielders = team.players.filter(type="MID")
            goalkeeper = team.players.filter(type="GK")
            '''
            f1 = Players.objects.filter(name=forward1)
            f2 = Players.objects.filter(name=forward2)
            d1 = Players.objects.filter(name=defender1)
            d2 = Players.objects.filter(name=defender2)
            d3 = Players.objects.filter(name=defender3)
            d4 = Players.objects.filter(name=defender4)
            m1 = Players.objects.filter(name=midfielder1)
            m2 = Players.objects.filter(name=midfielder2)
            m3 = Players.objects.filter(name=midfielder3)
            m4 = Players.objects.filter(name=midfielder4)
            g1 = Players.objects.filter(name=goalkeeper1)
            g2 = Players.objects.filter(name=goalkeeper2)
            # print(team.players.filter(type='FWD'))
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            gg1 = team.players.filter(type="GK")[0]
            gg2 = team.players.filter(type="GK")[1]
            # for f in f1:  # kane
            # team.players.add(Players.objects.get(id=f2[0].id))
            # ff = team.players.filter(type='FWD')[0]
            # for f in f2:
            # for ff in forwards:
            # print(ff.id)

            def ford(f, ff):
                if (f[0] == ff1 or f[0] == ff2):
                    print('already present')
                else:
                    team.players.add(Players.objects.get(id=f[0].id))
                    team.players.remove(Players.objects.get(id=ff.id))

            def defend(d, dd):
                if (d[0] == dd1 or d[0] == dd2 or d[0] == dd3 or d[0] == dd4):
                    print('already present')
                else:
                    team.players.remove(Players.objects.get(id=dd.id))
                    team.players.add(Players.objects.get(id=d[0].id))

            def mid(m, mm):
                if (m[0] == mm1 or m[0] == mm2 or m[0] == mm3 or m[0] == mm4):
                    print('already present')
                else:
                    team.players.remove(Players.objects.get(id=mm.id))
                    team.players.add(Players.objects.get(id=m[0].id))

            def goal(g, gg):
                if (g[0] == gg1 or g[0] == gg2):
                    print('already present')
                else:
                    team.players.add(Players.objects.get(id=g[0].id))
                    team.players.remove(Players.objects.get(id=gg.id))
            ford(f1, ff1)
            ford(f2, ff2)
            defend(d1, dd1)
            defend(d2, dd2)
            defend(d3, dd3)
            defend(d4, dd4)
            mid(m1, mm1)
            mid(m2, mm2)
            mid(m3, mm3)
            mid(m4, mm4)
            goal(g1, gg1)
            goal(g2, gg2)
            return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
        player = Players.objects.all()
        context = {
            # 'team': team,
            'player': player,
            'respond': respond,
        }
        return render(request, 'players/index.html', context)


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            n_user = request.user
            team = Team.objects.filter(user__username=n_user)
            if len(team) > 0:
                team_id = team[0].id
            context = {
                'user': request.user,
                'team_id': team_id,
            }
            return render(request, 'players/home.html', context)
        return render(request, 'players/home.html')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('User not found.Recheck or create a new account')
        return HttpResponse("Invalid, Login Again!!")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        form = RegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        forwards = Players.objects.filter(type='FWD')[:2]
        defenders = Players.objects.filter(type='DEF')[:4]
        mid = Players.objects.filter(type='MID')[:4]
        goalkeep = Players.objects.filter(type='GK')[:2]

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            team_name = form.cleaned_data['team']
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            team = Team(name=team_name, total_points=0, user=new_user)
            team.save()
            for f in forwards:
                team.players.add(f)
            for d in defenders:
                team.players.add(d)
            for m in mid:
                team.players.add(m)
            for g in goalkeep:
                team.players.add(g)
            return HttpResponseRedirect(reverse('login'))
        return HttpResponse("Form not filled properly")


class TeamView(View):
    def get(self, request, team_id):
        # n_user = request.user
        total_point = 0
        # team = Team.objects.filter(user__username=n_user)
        team = Team.objects.get(pk=team_id)
        players = team.players.all()
        # print(team.players.filter(type='FWD'))
        # print(team_id)
        # print(players)
        for player in players:
            total_point += player.points
        # print(total_point)
        names = team
        context = {
            'players': players,
            'name': names,
            'team_id': team_id,
            'total': total_point,
        }
        return render(request, 'players/teamsheet.html', context)
