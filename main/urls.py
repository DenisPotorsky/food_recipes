from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('log_in/', views.registration, name='login'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('all_recipes/', views.all_recipes, name='all_recipes'),
    path('personal_area/', views.personal_area, name='personal_area'),
    path('update_recipe/<int:pk>', views.update_recipe, name='update_recipe'),
    path('full/<int:pk>', views.full_recipe, name='full')
]

