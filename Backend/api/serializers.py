from rest_framework.serializers import ModelSerializer
from .models import Movie, Rating


class MovieSerializer(ModelSerializer):
	class Meta:
		model = Movie
		fields = '__all__'


class RatingSerializer(ModelSerializer):
	class Meta:
		model = Rating
		fields = '__all__'
