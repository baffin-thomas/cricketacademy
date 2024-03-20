from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('ground/',views.ground,name='ground'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('search/', views.search, name='search'),
    path('login/', views.login,name='login')
]


