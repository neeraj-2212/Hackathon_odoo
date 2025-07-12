
from django.urls import path,include
from . import views

urlpatterns = [

     path('login/', views.login_view, name='login'),
     path('', views.landing_page, name='landing'),   
     path('register/', views.register_view, name='register'),
     path('register/', views.register_view, name='register'),
     path('add_item/',views.add_item_view,name="add_item")
]
