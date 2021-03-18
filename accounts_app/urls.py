from django.urls import path
from .views import *


app_name='accounts_app'

urlpatterns = [
    path('registration/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    # path('registration/', UserRegisterView.as_view(), name='register'),

]

