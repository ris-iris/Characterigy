from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.first_page, name='firstpage'),
    path('login', views.log_in, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign_in/', views.signin, name='signin'),
    path('<int:user_id>/', views.user, name='user'),
    path('<int:user_id>/character/<int:character_id>/', views.character, name='character'),
    path('<int:user_id>/edit/', views.create_character, name='edit'),
]
