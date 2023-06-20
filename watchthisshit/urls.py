from django.urls import path
from .views import dashboard, profile_list, profile, recommendation

app_name = "watchthisshit"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("recommendation/<int:pk>/", recommendation, name="recommendation"),
]