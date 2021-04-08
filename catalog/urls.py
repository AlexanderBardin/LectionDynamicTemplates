from django.urls import path
from catalog import views

urlpatterns = [
    path("datetime/", views.new_view, name="date-time"),
    path("detail/", views.detail, name="detail")
]

