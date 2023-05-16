from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="Home"),
    path('signup/', views.signup,name="signup"),
    path('signin/', views.signin,name="signin"),
    path('logout/',views.LogoutPage,name='logout'),

]
