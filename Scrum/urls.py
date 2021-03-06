from django.urls import path
from . import views
app_name = "Scrum"

urlpatterns = [
    path('create_user/', views.create_user, name="create_user"),
    path('init_user/', views.init_user, name="init_user"),
    path('scrum_login', views.scrum_login, name="scrum_login"),
    path('scrum_logout', views.scrum_logout, name="scrum_logout"),
    path('profile/', views.profile, name="profile"),
    path('add_goal/', views.add_goal, name="add_goal"),
    path('remove_goal/<int:goal_id>/', views.remove_goal, name="remove_goal"),
    path('move_goal/<int:goal_id>/<int:to_id>/', views.move_goal, name="move_goal"),
    
]