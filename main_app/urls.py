from django.urls import path
from . import views # import views to connect routes to view functions

urlpatterns = {
    # routes will be added here
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
}