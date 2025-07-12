
from django.urls import path,include
from . import views

urlpatterns = [

     path('login/', views.login_view, name='login'),
     path('', views.landing_page, name='landing'),   
     path('register/', views.register_view, name='register'),
     path('register/', views.register_view, name='register'),
     path('add_item/',views.add_item_view,name="add_item"),
    path('items/', views.list_item_view, name='item-list'),
    path('items/<int:item_id>/',views.item_detail_view, name='item_detail'),
    path('profile/', views.user_profile, name='user_profile'),
   path('logout/', views.user_logout, name='logout'),
]
