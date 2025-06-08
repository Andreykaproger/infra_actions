from . import views
from django.urls import path

app_name = 'infra_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('second_page/', views.second_page, name='second_page'),

]
