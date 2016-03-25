from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^member/view_all', views.list_members),
    url(r'^member/post', views.post_member),
]
