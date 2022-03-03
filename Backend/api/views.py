from rest_framework.viewsets import ModelViewSet
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer


class MovieViewSet(ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer


class RatingViewSet(MovieViewSet):
	queryset = Rating.objects.all()
	serializer_class = RatingSerializer
