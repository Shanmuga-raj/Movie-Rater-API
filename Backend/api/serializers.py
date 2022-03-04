from rest_framework.serializers import ModelSerializer
from .models import Movie, Rating


class MovieSerializer(ModelSerializer):
	class Meta:
		model = Movie
		fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating')


class RatingSerializer(ModelSerializer):
	class Meta:
		model = Rating
		fields = ('id', 'movie', 'user', 'stars')