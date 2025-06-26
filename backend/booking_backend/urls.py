"""URL configuration for the booking_backend project.

It connects views to routes and integrates
with the frontend routing where applicable.
"""

from django.contrib import admin
from django.urls import path, include
from .views import omdb_movies_view, health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/omdb-movies/", omdb_movies_view, name="omdb-movies"),
    path('api/accounts/', include('accounts.urls')),
    path('health/', health_check)
]

handler404= 'booking_backend.views.custom_404_view'
