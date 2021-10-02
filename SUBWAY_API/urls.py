from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('swipe_in/', views.swipe_in),
    path('swipe_out/', views.swipe_out)
]
