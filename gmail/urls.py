from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home, name='home'),
    path("registration/", registraion, name="registration"),
    path("confirm_email/", confirm_email, name="confirm_email"),
    path("login/", login_user, name="login"),
    path("profile/", show_profile, name="profile"),
    path('send-all/', send_oll_mesage_for_our, name='send_all'),
]