from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:team_id>/', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('team/<int:team_id>', views.TeamView.as_view(), name='team'),
    path('status/', views.StatusView.as_view(), name="status"),
    path('fixtures/', views.FixturesView.as_view(), name="fixtures"),
    path('pickteam/<int:team_id>', views.PickTeamView.as_view(), name="transfer"),
    path('help/<int:team_id>', views.HelpView.as_view(), name="help"),
    # path('edit/<int:player_id>',
    #      views.edit, name='edit'),
    path('dreamteam/<int:team_id>',
         views.DreamTeamView.as_view(), name="dreamteam"),
    path('league/<int:team_id>', views.LeagueView.as_view(), name='league'),
    path('predict/<int:team_id>', views.PredictionView.as_view(), name='predict'),
]
