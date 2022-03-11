from multiprocessing import context
from unittest.case import DIFF_OMITTED
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Players, Team
from django.views.generic import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth import get_user_model
import pandas as pd
# import requests
# import csv
# import pandas as pd
# Create your views here.

# https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2021-22/gws/merged_gw.csv


class StatusView(View):
    def get(self, request):
        if request.user.is_authenticated:
            n_user = request.user
            team = Team.objects.filter(user__username=n_user)
            for t in team:
                team_id = t.id
            context = {
                'team_id': team_id,
            }
            return render(request, 'players/status.html', context)
        else:
            return render(request, 'players/status.html')


class FixturesView(View):
    def get(self, request):
        if request.user.is_authenticated:
            n_user = request.user
            team = Team.objects.filter(user__username=n_user)
            for t in team:
                team_id = t.id
            context = {
                'team_id': team_id,
            }
            return render(request, 'players/fixtures.html', context)
        else:
            return render(request, 'players/fixtures.html')


class IndexView(View):
    def get(self, request, team_id):
        # gk = request.POST.get('goalkeeper')
        # def1 = request.POST.get('defender1')
        n_user = request.user
        team = Team.objects.get(user__username=n_user)
        # team_players = team.players.all()
        player = Players.objects.all()
        ff1 = team.players.filter(type="FWD")[0]
        ff2 = team.players.filter(type="FWD")[1]
        # ff3 = team.players.filter(type="FWD")[2]
        dd1 = team.players.filter(type="DEF")[0]
        dd2 = team.players.filter(type="DEF")[1]
        dd3 = team.players.filter(type="DEF")[2]
        dd4 = team.players.filter(type="DEF")[3]
        # dd5 = team.players.filter(type="DEF")[4]
        mm1 = team.players.filter(type="MID")[0]
        mm2 = team.players.filter(type="MID")[1]
        mm3 = team.players.filter(type="MID")[2]
        mm4 = team.players.filter(type="MID")[3]
        gg1 = team.players.filter(type="GK")[0]
        ex_f = team.subs.filter(type="FWD")[0]
        ex_m = team.subs.filter(type="MID")[0]
        ex_d = team.subs.filter(type="DEF")[0]
        ex_g = team.subs.filter(type="GK")[0]
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
            'ff1': ff1,
            'ff2': ff2,
            'dd1': dd1,
            'dd2': dd2,
            'dd3': dd3,
            'dd4': dd4,
            'mm1': mm1,
            'mm2': mm2,
            'mm3': mm3,
            'mm4': mm4,
            'gg1': gg1,
            'ex_f': ex_f,
            'ex_m': ex_m,
            'ex_d': ex_d,
            'ex_g': ex_g,
            # 'response': response,
            # 'forward1': forward1,
            # 'forward2': forward2,
        }
        return render(request, 'players/index.html', context)

    def post(self, request, team_id):
        team = Team.objects.get(pk=team_id)
        forward1 = request.POST.get('forward1')
        forward2 = request.POST.get('forward2')
        forward3 = request.POST.get('extra4')
        defender1 = request.POST.get('defender1')
        defender2 = request.POST.get('defender2')
        defender3 = request.POST.get('defender3')
        defender4 = request.POST.get('defender4')
        defender5 = request.POST.get('extra2')
        midfielder1 = request.POST.get('mid-fielder1')
        midfielder2 = request.POST.get('mid-fielder2')
        midfielder3 = request.POST.get('mid-fielder3')
        midfielder4 = request.POST.get('mid-fielder4')
        midfielder5 = request.POST.get('extra3')
        goalkeeper1 = request.POST.get('goalkeeper1')
        goalkeeper2 = request.POST.get('extra1')
        # filtering players
        f1 = Players.objects.filter(name=forward1)
        f2 = Players.objects.filter(name=forward2)
        f3 = Players.objects.filter(name=forward3)
        d1 = Players.objects.filter(name=defender1)
        d2 = Players.objects.filter(name=defender2)
        d3 = Players.objects.filter(name=defender3)
        d4 = Players.objects.filter(name=defender4)
        d5 = Players.objects.filter(name=defender5)
        m1 = Players.objects.filter(name=midfielder1)
        m2 = Players.objects.filter(name=midfielder2)
        m3 = Players.objects.filter(name=midfielder3)
        m4 = Players.objects.filter(name=midfielder4)
        m5 = Players.objects.filter(name=midfielder5)
        g1 = Players.objects.filter(name=goalkeeper1)
        g2 = Players.objects.filter(name=goalkeeper2)
        # print(team.players.filter(type='FWD'))
        ff1 = team.players.filter(type="FWD")[0]
        ff2 = team.players.filter(type="FWD")[1]
        # ff3 = team.players.filter(type="FWD")[2]
        dd1 = team.players.filter(type="DEF")[0]
        dd2 = team.players.filter(type="DEF")[1]
        dd3 = team.players.filter(type="DEF")[2]
        dd4 = team.players.filter(type="DEF")[3]
        # dd5 = team.players.filter(type="DEF")[4]
        mm1 = team.players.filter(type="MID")[0]
        mm2 = team.players.filter(type="MID")[1]
        mm3 = team.players.filter(type="MID")[2]
        mm4 = team.players.filter(type="MID")[3]
        # mm5 = team.players.filter(type="MID")[4]
        gg1 = team.players.filter(type="GK")[0]
        # gg2 = team.players.filter(type="GK")[1]
        ex_f = team.subs.filter(type="FWD")[0]
        ex_m = team.subs.filter(type="MID")[0]
        ex_d = team.subs.filter(type="DEF")[0]
        ex_g = team.subs.filter(type="GK")[0]
        # if goalkeeper1:
        #     print(goalkeeper1)
        # f1 = Players.objects.filter(name=forward1)
        # if not f1:
        #     print("No forward")
        # if defender1:
        #     print(defender1)

        '''
        forwards = team.players.filter(type="FWD")
        defenders = team.players.filter(type="DEF")
        midfielders = team.players.filter(type="MID")
        goalkeeper = team.players.filter(type="GK")
        '''
        # for f in f1:  # kane
        #     team.players.add(Players.objects.get(id=f2[0].id))
        #     ff = team.players.filter(type='FWD')[0]
        # for f in f2:
        #     for ff in forwards:
        #         print(ff.id)
        def ford(f, ff):
            if (f[0] == ff1 or f[0] == ff2):  # or f[0] == ff3):
                print('already present')
                return True
            else:
                team.players.add(Players.objects.get(id=f[0].id))
                team.players.remove(Players.objects.get(id=ff.id))
                team.transfer_counter -= 1
                team.save()
                return False

        def defend(d, dd):
            if (d[0] == dd1 or d[0] == dd2 or d[0] == dd3 or d[0] == dd4):
                print('already present')
                return True
            else:
                team.players.remove(Players.objects.get(id=dd.id))
                team.players.add(Players.objects.get(id=d[0].id))
                team.transfer_counter -= 1
                team.save()
                return False

        def mid(m, mm):
            if (m[0] == mm1 or m[0] == mm2 or m[0] == mm3 or m[0] == mm4):
                print('already present')
                return True
            else:
                team.players.remove(Players.objects.get(id=mm.id))
                team.players.add(Players.objects.get(id=m[0].id))
                team.transfer_counter -= 1
                team.save()
                return False

        def goal(g, gg):
            if (g[0] == gg1):  # or g[0] == gg2):
                print('already present')
                return True
            else:
                team.players.add(Players.objects.get(id=g[0].id))
                team.players.remove(Players.objects.get(id=gg.id))
                team.transfer_counter -= 1
                team.save()
                return False

        def extra(e, ee):
            if (e[0] == (gg1 or mm1 or mm2 or mm3 or mm4 or dd1 or dd2 or dd3 or dd4 or ff1 or ff2)):
                print('already present')
                return True
            else:
                team.subs.add(Players.objects.get(id=e[0].id))
                team.subs.remove(Players.objects.get(id=ee.id))
                team.transfer_counter -= 1
                team.save()
                return False

        def club_counter(a):
            counter = 1
            for x in a:
                count = 0
                for y in a:
                    if x == y:
                        count += 1
                if count > 3:
                    counter = 0
            print(counter)
            return counter

        if f1:
            # ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = f1[0].price+ff2.price+ex_f.price+dd1.price + dd2.price + \
                dd3.price+dd4.price+ex_d.price + mm1.price + \
                mm2.price+mm3.price+mm4.price + \
                ex_m.price+gg1.price+ex_g.price
            print("{:.2f}".format(total_price))
            clubs = [f1[0].club, ff2.club, ex_f.club, dd1.club, dd2.club, dd3.club, dd4.club,
                     ex_d.club, mm1.club, mm2.club, mm3.club, mm4.club, ex_m.club, gg1.club, ex_g.club]
            print(club_counter(clubs))
            if club_counter(clubs):
                if f1 == ff2 or ex_f == f1 or ex_f == ff2 or mm1 == mm2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4 or ex_d == dd1 or ex_d == dd2 or ex_d == dd3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        ford(f1, ff1)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if f2:
            ff1 = team.players.filter(type="FWD")[0]
            # ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+f2[0].price+ex_f.price+dd1.price + dd2.price + \
                dd3.price+dd4.price+ex_d.price + mm1.price + \
                mm2.price+mm3.price+mm4.price + \
                ex_m.price+gg1.price+ex_g.price
            clubs = [ff1.club, f2[0].club, ex_f.club, dd1.club, dd2.club, dd3.club, dd4.club,
                     ex_d.club, mm1.club, mm2.club, mm3.club, mm4.club, ex_m.club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == f2 or ex_f == ff1 or ex_f == f2 or mm1 == mm2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4 or ex_d == dd1 or ex_d == dd2 or ex_d == dd3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        ford(f2, ff2)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if d1:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            # dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+ff2.price+ex_f.price+d1[0].price + dd2.price + \
                dd3.price+dd4.price+ex_d.price + mm1.price + \
                mm2.price+mm3.price+mm4.price + \
                ex_m.price+gg1.price+ex_g.price
            clubs = [ff1.club, ff2.club, ex_f.club, d1[0].club, dd2.club, dd3.club, dd4.club,
                     ex_d.club, mm1.club, mm2.club, mm3.club, mm4.club, ex_m.club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or ex_f == ff1 or ex_f == ff2 or mm1 == mm2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif d1 == dd2 or d1 == dd3 or d1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4 or ex_d == d1 or ex_d == dd2 or ex_d == dd3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        defend(d1, dd1)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if d2:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            # dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+ff2.price+ex_f.price+dd1.price + d2[0].price + \
                dd3.price+dd4.price+ex_d.price + mm1.price + \
                mm2.price+mm3.price+mm4.price + \
                ex_m.price+gg1.price+ex_g.price
            clubs = [ff1.club, ff2.club, ex_f.club, dd1.club, d2[0].club, dd3.club, dd4.club,
                     ex_d.club, mm1.club, mm2.club, mm3.club, mm4.club, ex_m.club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or ex_f == ff1 or ex_f == ff2 or mm1 == mm2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == d2 or dd1 == dd3 or dd1 == dd4 or d2 == dd3 or d2 == dd4 or dd3 == dd4 or ex_d == dd1 or ex_d == d2 or ex_d == dd3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        defend(d2, dd2)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if d3:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            # dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+ff2.price+ex_f.price+dd1.price + dd2.price + \
                d3[0].price+dd4.price+ex_d.price + mm1.price + \
                mm2.price+mm3.price+mm4.price + \
                ex_m.price+gg1.price+ex_g.price
            clubs = [ff1.club, ff2.club, ex_f.club, dd1.club, dd2.club, d3[0].club, dd4.club,
                     ex_d.club, mm1.club, mm2.club, mm3.club, mm4.club, ex_m.club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or ex_f == ff1 or ex_f == ff2 or mm1 == mm2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == d3 or dd1 == dd4 or dd2 == d3 or dd2 == dd4 or d3 == dd4 or ex_d == dd1 or ex_d == dd2 or ex_d == d3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        defend(d3, dd3)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if d4:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            # dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+ff2.price+ex_f.price+dd1.price + dd2.price + \
                dd3.price+d4[0].price+ex_d.price + mm1.price + \
                mm2.price+mm3.price+mm4.price + \
                ex_m.price+gg1.price+ex_g.price
            clubs = [ff1.club, ff2.club, ex_f.club, dd1.club, dd2.club, dd3.club, d4[0].club,
                     ex_d.club, mm1.club, mm2.club, mm3.club, mm4.club, ex_m.club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or ex_f == ff1 or ex_f == ff2 or mm1 == mm2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == d4 or dd2 == dd3 or dd2 == d4 or dd3 == d4 or ex_d == dd1 or ex_d == dd2 or ex_d == dd3 or ex_d == d4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        defend(d4, dd4)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if m1:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            # mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+ff2.price+ex_f.price+dd1.price + dd2.price + \
                dd3.price+dd4.price+ex_d.price + m1[0].price + \
                mm2.price+mm3.price+mm4.price + \
                ex_m.price+gg1.price+ex_g.price
            clubs = [ff1.club, ff2.club, ex_f.club, dd1.club, dd2.club, dd3.club, dd4.club,
                     ex_d.club, m1[0].club, mm2.club, mm3.club, mm4.club, ex_m.club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or ex_f == ff1 or ex_f == ff2 or m1 == mm2 or mm3 == mm4 or m1 == mm3 or m1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == m1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4 or ex_d == dd1 or ex_d == dd2 or ex_d == dd3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        mid(m1, mm1)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if m2:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            # mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+ff2.price+ex_f.price+dd1.price + dd2.price + \
                dd3.price+dd4.price+ex_d.price + mm1.price + \
                m2[0].price+mm3.price+mm4.price + \
                ex_m.price+gg1.price+ex_g.price
            clubs = [ff1.club, ff2.club, ex_f.club, dd1.club, dd2.club, dd3.club, dd4.club,
                     ex_d.club, mm1.club, m2[0].club, mm3.club, mm4.club, ex_m.club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or ex_f == ff1 or ex_f == ff2 or mm1 == m2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or m2 == mm3 or m2 == mm4 or ex_m == mm1 or ex_m == m2 or ex_m == m3 or ex_m == m4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4 or ex_d == dd1 or ex_d == dd2 or ex_d == dd3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        mid(m2, mm2)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if m3:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            # mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+ff2.price+ex_f.price+dd1.price + dd2.price + \
                dd3.price+dd4.price+ex_d.price + mm1.price + \
                mm2.price+m3[0].price+mm4.price + \
                ex_m.price+gg1.price+ex_g.price
            clubs = [ff1.club, ff2.club, ex_f.club, dd1.club, dd2.club, dd3.club, dd4.club,
                     ex_d.club, mm1.club, mm2.club, m3[0].club, mm4.club, ex_m.club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or ex_f == ff1 or ex_f == ff2 or mm1 == mm2 or m3 == m4 or mm1 == m3 or mm1 == m4 or mm2 == m3 or mm2 == m4 or ex_m == mm1 or ex_m == mm2 or ex_m == m3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        mid(m3, mm3)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if m4:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            # mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+ff2.price+ex_f.price+dd1.price + dd2.price + \
                dd3.price+dd4.price+ex_d.price + mm1.price + \
                mm2.price+mm3.price+m4[0].price + \
                ex_m.price+gg1.price+ex_g.price
            clubs = [ff1.club, ff2.club, ex_f.club, dd1.club, dd2.club, dd3.club, dd4.club,
                     ex_d.club, mm1.club, mm2.club, mm3.club, m4[0].club, ex_m.club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or mm1 == mm2 or mm3 == m4 or mm1 == mm3 or mm1 == m4 or mm2 == mm3 or mm2 == m4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == m4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4 or ex_d == dd1 or ex_d == dd2 or ex_d == dd3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        mid(m4, mm4)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if g1:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            # gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            print(ff1)
            total_price = ff1.price+ff2.price+ex_f.price+dd1.price + dd2.price + \
                dd3.price+dd4.price+ex_d.price + mm1.price + \
                mm2.price+mm3.price+mm4.price + \
                ex_m.price+g1[0].price+ex_g.price
            clubs = [ff1.club, ff2.club, ex_f.club, dd1.club, dd2.club, dd3.club, dd4.club,
                     ex_d.club, mm1.club, mm2.club, mm3.club, mm4.club, ex_m.club, g1[0].club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or ex_f == ff1 or ex_f == ff2 or mm1 == mm2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4 or ex_d == dd1 or ex_d == dd2 or ex_d == dd3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif g1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        goal(g1, gg1)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if d5:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            # ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+ff2.price+ex_f.price+dd1.price + dd2.price + \
                dd3.price+dd4.price+d5[0].price + mm1.price + \
                mm2.price+mm3.price+mm4.price + \
                ex_m.price+gg1.price+ex_g.price
            clubs = [ff1.club, ff2.club, ex_f.club, dd1.club, dd2.club, dd3.club, dd4.club,
                     d5[0].club, mm1.club, mm2.club, mm3.club, mm4.club, ex_m.club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or ex_f == ff1 or ex_f == ff2 or mm1 == mm2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4 or ex_d == dd1 or ex_d == dd2 or ex_d == dd3 or ex_d == dd4 or ex_d == d5:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        extra(d5, ex_d)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if f3:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            # ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+ff2.price+f3[0].price+dd1.price + dd2.price + \
                dd3.price+dd4.price+ex_d.price + mm1.price + \
                mm2.price+mm3.price+mm4.price + \
                ex_m.price+gg1.price+ex_g.price
            clubs = [ff1.club, ff2.club, f3[0].club, dd1.club, dd2.club, dd3.club, dd4.club,
                     ex_d.club, mm1.club, mm2.club, mm3.club, mm4.club, ex_m.club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or f3 == ff1 or f3 == ff2 or mm1 == mm2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4 or ex_d == dd1 or ex_d == dd2 or ex_d == dd3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        extra(f3, ex_f)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if m5:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            # ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            ex_g = team.subs.filter(type="GK")[0]
            print(ff1)
            total_price = ff1.price+ff2.price+ex_f.price+dd1.price + dd2.price + \
                dd3.price+dd4.price+ex_d.price + mm1.price + \
                mm2.price+mm3.price+mm4.price + \
                m5[0].price+gg1.price+ex_g.price
            clubs = [ff1.club, ff2.club, ex_f.club, dd1.club, dd2.club, dd3.club, dd4.club,
                     ex_d.club, mm1.club, mm2.club, mm3.club, mm4.club, m5[0].club, gg1.club, ex_g.club]
            if club_counter(clubs):
                if ff1 == ff2 or ex_f == ff1 or ex_f == ff2 or mm1 == mm2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4 or ex_d == dd1 or ex_d == dd2 or ex_d == dd3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == ex_g:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        extra(m5, ex_m)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        if g2:
            ff1 = team.players.filter(type="FWD")[0]
            ff2 = team.players.filter(type="FWD")[1]
            # ff3 = team.players.filter(type="FWD")[2]
            dd1 = team.players.filter(type="DEF")[0]
            dd2 = team.players.filter(type="DEF")[1]
            dd3 = team.players.filter(type="DEF")[2]
            dd4 = team.players.filter(type="DEF")[3]
            # dd5 = team.players.filter(type="DEF")[4]
            mm1 = team.players.filter(type="MID")[0]
            mm2 = team.players.filter(type="MID")[1]
            mm3 = team.players.filter(type="MID")[2]
            mm4 = team.players.filter(type="MID")[3]
            # mm5 = team.players.filter(type="MID")[4]
            gg1 = team.players.filter(type="GK")[0]
            # gg2 = team.players.filter(type="GK")[1]
            ex_f = team.subs.filter(type="FWD")[0]
            ex_m = team.subs.filter(type="MID")[0]
            ex_d = team.subs.filter(type="DEF")[0]
            # ex_g = team.subs.filter(type="GK")[0]
            total_price = ff1.price+ff2.price+ex_f.price+dd1.price + dd2.price + \
                dd3.price+dd4.price+ex_d.price + mm1.price + \
                mm2.price+mm3.price+mm4.price + \
                ex_m.price+gg1.price+g2[0].price
            clubs = [ff1.club, ff2.club, ex_f.club, dd1.club, dd2.club, dd3.club, dd4.club,
                     ex_d.club, mm1.club, mm2.club, mm3.club, mm4.club, ex_m.club, gg1.club, g2[0].club]
            if club_counter(clubs):
                if ff1 == ff2 or ex_f == ff1 or ex_f == ff2 or mm1 == mm2 or mm3 == mm4 or mm1 == mm3 or mm1 == mm4 or mm2 == mm3 or mm2 == mm4 or ex_m == mm1 or ex_m == mm2 or ex_m == mm3 or ex_m == mm4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif dd1 == dd2 or dd1 == dd3 or dd1 == dd4 or dd2 == dd3 or dd2 == dd4 or dd3 == dd4 or ex_d == dd1 or ex_d == dd2 or ex_d == dd3 or ex_d == dd4:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                elif gg1 == g2:
                    respond = "You cannot choose the same players more than once. Choose the another one."
                else:
                    respond = ''
                    if total_price <= 100:
                        extra(g2, ex_g)
                        return HttpResponseRedirect('/players/team/{}'.format(str(team_id)))
                    else:
                        war = 'You are out of budget. Please pick your team again.'
                        context = {
                            'warning': war,
                            'team_id': team_id,
                        }
                    return render(request, 'players/teamsheet.html', context)
            else:
                respond = "You cannot choose more than three players from same team"
        player = Players.objects.all()
        context = {
            'team': team,
            'respond': respond,
            'team': team,
            'player': player,
            'team_id': team_id,
            'ff1': ff1,
            'ff2': ff2,
            'dd1': dd1,
            'dd2': dd2,
            'dd3': dd3,
            'dd4': dd4,
            'mm1': mm1,
            'mm2': mm2,
            'mm3': mm3,
            'mm4': mm4,
            'gg1': gg1,
            'ex_f': ex_f,
            'ex_m': ex_m,
            'ex_d': ex_d,
            'ex_g': ex_g,
            # 'transfer_counter': transfer_count,
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
                return HttpResponseRedirect(reverse('status'))
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
        player = Players.objects.all()
        context = {
            'form': form,
            'player': player,
        }
        return render(request, 'register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            team_name = form.cleaned_data['team']
            forward1 = request.POST.get('forward1')
            forward2 = request.POST.get('forward2')
            forward3 = request.POST.get('extra4')
            defender1 = request.POST.get('defender1')
            defender2 = request.POST.get('defender2')
            defender3 = request.POST.get('defender3')
            defender4 = request.POST.get('defender4')
            defender5 = request.POST.get('extra2')
            midfielder1 = request.POST.get('mid-fielder1')
            midfielder2 = request.POST.get('mid-fielder2')
            midfielder3 = request.POST.get('mid-fielder3')
            midfielder4 = request.POST.get('mid-fielder4')
            midfielder5 = request.POST.get('extra3')
            goalkeeper1 = request.POST.get('goalkeeper1')
            goalkeeper2 = request.POST.get('extra1')
            f1 = Players.objects.filter(name=forward1)
            f2 = Players.objects.filter(name=forward2)
            f3 = Players.objects.filter(name=forward3)
            d1 = Players.objects.filter(name=defender1)
            d2 = Players.objects.filter(name=defender2)
            d3 = Players.objects.filter(name=defender3)
            d4 = Players.objects.filter(name=defender4)
            d5 = Players.objects.filter(name=defender5)
            m1 = Players.objects.filter(name=midfielder1)
            m2 = Players.objects.filter(name=midfielder2)
            m3 = Players.objects.filter(name=midfielder3)
            m4 = Players.objects.filter(name=midfielder4)
            m5 = Players.objects.filter(name=midfielder5)
            g1 = Players.objects.filter(name=goalkeeper1)
            g2 = Players.objects.filter(name=goalkeeper2)
            list = []
            list.append(f1)
            list.append(f2)
            list.append(f3)
            list.append(d1)
            list.append(d2)
            list.append(d3)
            list.append(d4)
            list.append(d5)
            list.append(m1)
            list.append(m2)
            list.append(m3)
            list.append(m4)
            list.append(m5)
            list.append(g1)
            list.append(g2)
            total = 0

            def club_counter(a):
                counter = 1
                for x in a:
                    count = 0
                    for y in a:
                        if x == y:
                            count += 1
                    if count > 3:
                        counter = 0
                print(counter)
                return counter

            for l in list:
                for p in l:
                    total += p.price
            remain = 100-total
            clubs = [f1[0].club, f2[0].club, f3[0].club, d1[0].club, d2[0].club, d3[0].club, d4[0].club,
                     d5[0].club, m1[0].club, m2[0].club, m3[0].club, m4[0].club, m5[0].club, g1[0].club, g2[0].club]
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            if club_counter(clubs):
                if f1[0] == f2[0] or f1[0] == f3[0] or f2[0] == f3[0]:
                    form = RegisterForm()
                    player = Players.objects.all()
                    response = "You cannot choose same player multiple times"
                    context = {
                        'form': form,
                        'player': player,
                        'response': response,
                        'remain': remain,
                    }
                    return render(request, 'register.html', context)
                elif d1[0] == d2[0] or d1[0] == d3[0] or d1[0] == d4[0] or d1[0] == d5[0] or d2[0] == d3[0] or d2[0] == d4[0] or d2[0] == d5[0] or d3[0] == d4[0] or d3[0] == d5[0] or d4[0] == d5[0]:
                    form = RegisterForm()
                    player = Players.objects.all()
                    response = "You cannot choose same player multiple times"
                    context = {
                        'form': form,
                        'player': player,
                        'response': response,
                        'remain': remain,
                    }
                    return render(request, 'register.html', context)
                elif m1[0] == m2[0] or m1[0] == m3[0] or m1[0] == m4[0] or m1[0] == m5[0] or m2[0] == m3[0] or m2[0] == m4[0] or m2[0] == m5[0] or m3[0] == m4[0] or m3[0] == m5[0] or m4[0] == m5[0]:
                    form = RegisterForm()
                    player = Players.objects.all()
                    response = "You cannot choose same player multiple times"
                    context = {
                        'form': form,
                        'player': player,
                        'response': response,
                        'remain': remain,
                    }
                    return render(request, 'register.html', context)
                elif g1[0] == g2[0]:
                    form = RegisterForm()
                    player = Players.objects.all()
                    response = "You cannot choose same player multiple times"
                    context = {
                        'form': form,
                        'player': player,
                        'response': response,
                        'remain': remain,
                    }
                    return render(request, 'register.html', context)
                elif total > 100:
                    response = "Choose Players within the budget of 100"
                    form = RegisterForm()
                    player = Players.objects.all()
                    context = {
                        'form': form,
                        'player': player,
                        'response': response,
                        'remain': remain,
                    }
                    return render(request, 'register.html', context)
                else:
                    new_user.save()
                    team = Team(name=team_name, total_points=0, user=new_user)
                    team.save()

                    def create_p(pp):
                        for p in pp:
                            team.players.add(p)

                    def create_e(ee):
                        for e in ee:
                            team.subs.add(e)
                    create_p(f1)
                    create_p(f2)
                    create_p(d1)
                    create_p(d2)
                    create_p(d3)
                    create_p(d4)
                    create_p(m1)
                    create_p(m2)
                    create_p(m3)
                    create_p(m4)
                    create_p(g1)
                    create_e(f3)
                    create_e(d5)
                    create_e(m5)
                    create_e(g2)
                    return HttpResponseRedirect(reverse('login'))
            else:
                response = 'You cannot choose players more than 3 from same teams.'
                form = RegisterForm()
                player = Players.objects.all()
                context = {
                    'form': form,
                    'player': player,
                    'response': response,
                }
                return render(request, 'register.html', context)
        return HttpResponse("Form not filled properly")


class TeamView(View):
    def get(self, request, team_id):
        # n_user = request.user
        total_point = 0
        total_price = 0
        # team = Team.objects.filter(user__username=n_user)
        team = Team.objects.get(pk=team_id)
        if team.user == request.user:
            players = team.players.all()
            print(len(players))
            extras = team.subs.all()
            print(len(extras))
            # print(team.players.filter(type='FWD'))
            # print(team_id)
            # print(players)
            forwards = []
            defenders = []
            midfields = []
            goalkeeps = []
            extra_f = []
            extra_d = []
            extra_m = []
            extra_g = []
            for player in players:
                if player.type == 'FWD':
                    if player.minutes > 0:
                        forwards.append(player)
                        print(player)
                    else:
                        for e in extras:
                            if e.type == 'FWD':
                                if e.minutes > 0 and (e not in forwards):
                                    print(e)
                                    forwards.append(e)
                                    if player not in extra_f:
                                        extra_f.append(player)
                                        print(player)
                                else:
                                    print(player)
                                    forwards.append(player)
                                    if (e not in extra_f) and (e not in forwards):
                                        extra_f.append(e)
                                        print(e)
                if player.type == 'DEF':
                    if player.minutes > 0:
                        defenders.append(player)
                        print(player)
                    else:
                        for e in extras:
                            if e.type == 'DEF':
                                if e.minutes > 0 and (e not in defenders):
                                    print(e)
                                    defenders.append(e)
                                    if player not in extra_d:
                                        extra_d.append(player)
                                        print(player)
                                else:
                                    print(player)
                                    defenders.append(player)
                                    if (e not in extra_d) and (e not in defenders):
                                        extra_d.append(e)
                                        print(e)
                                    # if player not in (d.name for d in defenders):
                                    #     print(player)
                                    #     defenders.append(player)
                if player.type == 'MID':
                    if player.minutes > 0:
                        midfields.append(player)
                        print(player)
                    else:
                        for e in extras:
                            if e.type == 'MID':
                                if e.minutes > 0 and (e not in midfields):
                                    print(e)
                                    midfields.append(e)
                                    if player not in extra_m:
                                        extra_m.append(player)
                                        print(player)
                                else:
                                    print(player)
                                    midfields.append(player)
                                    if (e not in extra_m) and (e not in midfields):
                                        extra_m.append(e)
                                        print(e)
                if player.type == 'GK':
                    if player.minutes > 0:
                        goalkeeps.append(player)
                        print(player)
                        for e in extras:
                            if e.type == 'GK':
                                extra_g.append(e)
                                print(e)
                    else:
                        for e in extras:
                            if e.type == 'GK':
                                if e.minutes > 0 and (e not in goalkeeps):
                                    goalkeeps.append(e)
                                    print(e)
                                    extra_g.append(player)
                                    print(player)
                                else:
                                    goalkeeps.append(player)
                                    extra_g.append(e)
                        # for e in extras:
                        #     if e.type == 'GK':
                        #         if e.minutes > 0 and (e not in goalkeeps):
                        #             print(e)
                        #             goalkeeps.append(e)
                        #             if player not in extra_g:
                        #                 extra_g.append(player)
                        #         else:
                        #             print(player)
                        #             goalkeeps.append(player)
                        #             if (e not in extra_g) and (e not in goalkeeps):
                        #                 extra_g.append(e)
            for e in extras:
                if e.type == 'FWD':
                    if (e not in forwards) and (e not in extra_f):
                        extra_f.append(e)
                        print(e)
                if e.type == 'DEF':
                    if (e not in defenders) and (e not in extra_d):
                        extra_d.append(e)
                        print(e)
                if e.type == 'MID':
                    if (e not in midfields) and (e not in extra_m):
                        extra_m.append(e)
                        print(e)
                if e.type == 'GK':
                    if (e not in goalkeeps) and (e not in extra_g):
                        extra_g.append(e)
                        print(e)
            print(forwards)
            print(midfields)
            print(defenders)
            print(goalkeeps)
            print(extra_f)
            print(extra_d)
            print(extra_m)
            print(extra_g)

            new_set = []
            new_set.append(forwards)
            new_set.append(midfields)
            new_set.append(defenders)
            new_set.append(goalkeeps)
            print(new_set)
            # for extra in extras:
            #     if extra.type == 'FWD':
            #         extra_f.append(extra)
            #     if extra.type == 'DEF':
            #         extra_d.append(extra)
            #     if extra.type == 'MID':
            #         extra_m.append(extra)
            #     if extra.type == 'GK':
            #         extra_g.append(extra)
            cap = team.captain
            for player in players:
                total_price += player.price
            for extra in extras:
                total_price += extra.price
            for n in new_set:
                for p in n:
                    if p == cap:
                        total_point += p.points*2
                    else:
                        total_point += p.points
            team.week_point = total_point
            team.squad_value = total_price
            team.save()
            print(team.week_point)
            # print(extra_g)
            # print(forwards)
            # print(defenders)
            # print(midfields)
            # print(goalkeeps)
            # print(total_point)
            if cap in players:
                cap = team.captain
            else:
                cap = None
            budget = 100-total_price
            budget = "{:.2f}".format(budget)
            names = team
            context = {
                # 'players': players,
                'name': names,
                'team_id': team_id,
                'total': total_point,
                # 'extras': extras,
                'total_price': total_price,
                'budget': budget,
                'for': forwards,
                'mid': midfields,
                'def': defenders,
                'gk': goalkeeps,
                'ex_f': extra_f,
                'ex_m': extra_m,
                'ex_d': extra_d,
                'ex_g': extra_g,
                'captain': cap,
            }
            return render(request, 'players/teamsheet.html', context)
        return HttpResponseRedirect('/players')


class PickTeamView(View):
    def get(self, request, team_id):
        # n_user = request.user
        team = Team.objects.get(id=team_id)
        r_players = team.players.all()
        r_extras = team.subs.all()
        c = team.captain
        context = {
            'players': r_players,
            'extras': r_extras,
            'team_id': team_id,
            'captain': c,
        }
        return render(request, 'players/pickteam.html', context)

    def post(self, request, team_id):
        captain = request.POST.get('captain')
        team = Team.objects.get(id=team_id)
        cap = Players.objects.filter(name=captain)
        for cc in cap:
            team.captain = cc
        team.save()
        r_players = team.players.all()
        r_extras = team.subs.all()
        c = team.captain
        context = {
            'players': r_players,
            'extras': r_extras,
            'team_id': team_id,
            'captain': c,
        }
        print(cap)
        return render(request, 'players/pickteam.html', context)


class LeagueView(View):
    def get(self, request, team_id):
        teams = Team.objects.all()
        lists = []
        # print(lists)
        #ordered_authors = Author.objects.order_by('-score', 'last_name')[:30]
        lists = Team.objects.order_by('-total_points')
        print(lists)
        context = {
            'team_id': team_id,
            'lis': lists,
        }
        return render(request, 'players/leagues.html', context)


class HelpView(View):
    def get(self, request, team_id):
        context = {
            'team_id': team_id,
        }
        return render(request, 'players/help.html', context)


class DreamTeamView(View):
    def get(self, request, team_id):
        df = pd.read_csv(
            'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2021-22/gws/gw25.csv')
        GK_filt = df['position'] == 'GK'
        mid_filt = df['position'] == 'MID'
        def_filt = df['position'] == 'DEF'
        fwd_filt = df['position'] == 'FWD'
        df_GK = df.loc[GK_filt, ['position', 'name', 'total_points']]
        df_mid = df.loc[mid_filt, ['position', 'name', 'total_points']]
        df_def = df.loc[def_filt, ['position', 'name', 'total_points']]
        df_fwd = df.loc[fwd_filt, ['position', 'name', 'total_points']]
        df_mid.sort_values(by=['total_points'], inplace=True, ascending=False)

        df_fwd.sort_values(by=['total_points'], inplace=True, ascending=False)
        df_def.sort_values(by=['total_points'], inplace=True, ascending=False)
        keeper = df_GK.loc[df_GK['total_points'].idxmax()]
        print(keeper)
        print(df_fwd)
        forward = df_fwd[0:4].name.tolist()
        midfield = df_mid[0:5].name.tolist()
        defender = df_def[0:5].name.tolist()
        print(forward)
        # for 433
        context = {
            'team_id': team_id,
            'keeper': keeper,
            'fwd': forward,
            'def': defender,
            'mid': midfield,
        }
        return render(request, 'players/dreamteam.html', context)
        # goalkeeper = []
        # forward = []
        # defender = []
        # mid = []
        # formation('fft')

        # def formation(x):
        #     if x == 'fft':
        #         # goalkeeper.append(keeper)
        #         # forward.append(df_fwd.head(3))
        #         # defender.append(df_def.head(4))
        #         # mid.append(df_mid.head(4))
        #         goalkeeper = keeper
        #         forward = df_fwd.head(3)
        #         defender = df_def.head(4)
        #         midfield = df_mid.head(4)
        #         context = {
        #             'team_id': team_id,
        #             'fwd': df_fwd,
        #             'goalkeeper': goalkeeper,
        #             'forward': forward,
        #             'midfield': midfield,
        #             'defender': defender,
        #         }
        #         return render(request, 'players/dreamteam.html', context)
