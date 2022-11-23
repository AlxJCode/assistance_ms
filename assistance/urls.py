from django.urls import path
from assistance.api_views.data_views import *


urlpatterns = [

    # 
    path('data/', DataView.as_view()),
]