from django.contrib import admin
from django.urls import path
from .views import omdb_movies_view, health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/omdb-movies/", omdb_movies_view, name="omdb-movies"),
    path('health/', health_check)
]

handler404= 'booking_backend.views.custom_404_view'
