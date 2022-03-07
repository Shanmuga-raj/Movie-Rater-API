from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
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


class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'password')
		extra_kwargs = {
			'password': {
				'write_only': True,
				'required': True
			}
		}

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		Token.objects.create(user=user)
		return user
