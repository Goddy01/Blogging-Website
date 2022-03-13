from django.urls import re_path
from blog_app.views import AboutView, PostListView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView, DeletePostView
# , RegisterProfileView

app_name = 'blog_app'

urlpatterns = [
    re_path('^about/$', AboutView.as_view(), name='about'),
    # re_path('^register/$', RegisterProfileView.as_view(), name='register'),
    re_path('^$', PostListView.as_view(), name='post_list'),
    re_path('^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    re_path('^post/new_post/$', CreatePostView.as_view(), name='create_post'),
    re_path('^post/update/(?P<pk>\d+)/edit/$', UpdatePostView.as_view(), name='update_post'),
    re_path('^post/(?P<pk>\d+/)/delete\$', DeletePostView.as_view(), name='delete_post'),
    re_path('^drafts/$', DeletePostView.as_view(), name='drafts')

]