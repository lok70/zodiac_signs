from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:zodiac_name>/', views.zodiac, name='zodiac'),
]

