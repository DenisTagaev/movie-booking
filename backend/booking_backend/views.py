from django.http import JsonResponse
from .utils.omdb_fetcher import fetch_random_omdb_movie

def omdb_movies_view(request):
    movie=fetch_random_omdb_movie()
    if movie:
        return JsonResponse(movie)
    return JsonResponse({"error": "Movie not found"}, status=404)