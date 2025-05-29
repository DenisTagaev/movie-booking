from django.http import JsonResponse
from .utils.omdb_fetcher import fetch_random_omdb_movie
from django.views.decorators.http import require_GET
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