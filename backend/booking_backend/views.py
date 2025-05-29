"""View functions for the movie booking backend.

Includes handlers for:
- OMDB movie fetching for test display
- Health check endpoint for container monitoring
- Custom error views (e.g., 404 JSON responses)
"""


from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .utils.omdb_fetcher import fetch_random_omdb_movie
@require_GET
def omdb_movies_view(request):
    movie=fetch_random_omdb_movie()
    if movie:
        return JsonResponse(movie)
    return JsonResponse({"error": "Movie not found"}, status=404)

def custom_404_view( request, exception ):
    return JsonResponse({'detail': 'Not Found'}, status=404)

def health_check(request):
    return JsonResponse({'status': 'ok'})
