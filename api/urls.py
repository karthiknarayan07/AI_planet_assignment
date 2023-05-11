from django.urls import path
from . import views

urlpatterns=[
    path('hackathons/<str:filterParam>', views.availableHackathons, name="availableHackathons"),
    path('hackathon/<str:action_name>/<int:hackathon_id>', views.viewApplyHackathons, name="viewApplyHackathons"),
    path('users/<str:user_filter>',views.usersList,name='usersList')
]