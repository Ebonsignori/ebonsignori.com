from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='posts'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<slug>[-\w]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<slug>[-\w]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<slug>[-\w]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<slug>[-\w]+)/restore/$', views.post_restore, name='post_restore'),
    url(r'^post/(?P<slug>[-\w]+)/delete$', views.post_delete, name='post_delete'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.post_view, name='post_view'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^deleted/$', views.post_deleted_list, name='post_deleted_list'),
]