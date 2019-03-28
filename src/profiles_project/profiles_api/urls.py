from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from . import views


route=DefaultRouter()
route.register('hello-viewset', views.HelloViewSet, base_name="hello-viewset")
route.register('profile', views.UserProfileViewSet)
route.register('login',views.LoginViewSet, base_name='login')
urlpatterns=[
    url(r'^hello-view/',views.HelloApiView.as_view()),
    url(r'',include(route.urls)),
]
