from api import views
from django.urls import path,include

urlpatterns = [
    path('', views.sign_up,name='signup'),
    path('accounts/', include('allauth.urls')),
    path('userlogin/',views.user_login,name='userlogin'),
    path('userprofile/',views.user_profile,name='userprofile'),
    path('userlogout/',views.user_logout,name='userlogout'),
    path('changepass/',views.user_changepass,name='changepass'),
]
