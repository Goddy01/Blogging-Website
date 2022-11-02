from django.urls import re_path
from blog_app.views import AboutView, PostListView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView, DeletePostView, CreateProfileView
from blog_site.blog_app.views import DeleteProfileView, add_comment_to_post, comment_remove, publish_post

app_name = 'blog_app'

urlpatterns = [
    re_path(r'^about/$', AboutView.as_view(), name='about'),
    re_path(r'^$', PostListView.as_view(), name='post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    re_path(r'^post/new_post/$', CreatePostView.as_view(), name='create_post'),
    re_path(r'^post/update/(?P<pk>\d+)/edit/$', UpdatePostView.as_view(), name='update_post'),
    re_path(r'^post/(?P<pk>\d+)/delete/$', DeletePostView.as_view(), name='delete_post'),
    re_path(r'^drafts/$', DeletePostView.as_view(), name='drafts'),
    re_path(r'^profile/create/$', CreateProfileView.as_view(), name='create_profile'),
    re_path(r'^profile/(?P<pk>\d+)/delete/$', DeleteProfileView.as_view(), name='delete_profile'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', add_comment_to_post, name='add_comment_to_post'),
    re_path(r'post/(?P<pk>\d+)/remove/$', comment_remove, name='remove_comment'),
    re_path(r'post/(?P<pk>\d+)/publish/$', publish_post, name='publish_post')
]