from django.urls import path
from .views import home,index, profile, RegisterView,logout_view
from . import views

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('logout_view/',logout_view,name='logout_view'),
    path('index/', index, name='users-index'),
    path('Deploy_8/',views.Deploy_8,name='Deploy_8'),
    path('Database',views.Database,name='Database'),
    
    
    ]


 