from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^member/view_all', views.MemberViewSet.list_members),
    url(r'^add_member', views.MemberViewSet.post_member),
    url(r'^attend_meeting', views.increment_attendance),
    url(r'^committee/join', views.CommitteeViewSet.join_committee),
]
