from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('hackathon/submit/<int:hackathon_id>', views.hackathonSubmit, name="hackathonSubmit"),
    path('hackathon/<int:hackathon_id>', views.hackathon, name="hackathon"),
    path('my_hackathons/<int:hackathon_id>', views.my_hackathons, name="my_hackathons"),
    path('create', views.createHackathon, name="createHackathon"),
    path('login', views.login_view, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_view, name="logout"),
]