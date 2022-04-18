from basic_app import views
from django.conf.urls import url, include

app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$', views.register, name='registration'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'^special/$', views.special, name='special'),
]