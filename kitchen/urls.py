from django.urls import path
from . import views

app_name = 'kitchen'

urlpatterns = [
    path('', views.choice_list, name='choice_list'),
    path('<slug:menu_slug>/', views.choice_list,
         name='choice_list_by_menu'),
    path('<int:id>/<slug:slug>/', views.choice_detail,
         name='choice_detail'),
]