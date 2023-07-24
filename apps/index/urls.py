from django.urls import path

from apps.index.views import IndexView, ProfileView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
