from django.urls import path
from .views import *

urlpatterns = [
   path('signup/', Signup.as_view()),
   path('login/', Login.as_view()),
   path('user/', UserView.as_view()),
   path('logout/', Logout.as_view()),
]
