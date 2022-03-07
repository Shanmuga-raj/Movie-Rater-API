from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer


class MovieViewSet(ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer
	filter_backends = (SearchFilter, )
	search_fields = ['title']
	authentication_classes = (TokenAuthentication, )
	permission_classes = (AllowAny, )

	@action(detail=True, methods=['POST'])
	def rate_movie(self, request, pk=None):
		if 'stars' in request.data:
			movie = Movie.objects.get(id=pk)
			stars = request.data['stars']
			user = request.user

			try:
				rating = Rating.objects.get(user=user.id, movie=movie.id)
				rating.stars = stars
				rating.save()

				serializer = RatingSerializer(rating, many=False)
				response = {'message': 'Rating Updated', 'result': serializer.data}
				return Response(response, status=status.HTTP_200_OK)

			except:
				rating = Rating.objects.create(user=user, movie=movie, stars=stars)
				serializer = RatingSerializer(rating, many=False)
				response = {'message': 'Rating Created', 'result': serializer.data}
				return Response(response, status=status.HTTP_201_CREATED)

		else:
			response = {'message': 'You need to provide stars to give rating'}
			return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(ModelViewSet):
	queryset = Rating.objects.all()
	serializer_class = RatingSerializer
	authentication_class = (TokenAuthentication, )
	permission_classes = (IsAuthenticated, )

	def create(self, request, *args, **kwargs):
		response = {'message': 'You cannot create rating directly!'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)

	def update(self, request, *args, **kwargs):
		response = {'message': 'You cannot update rating directly!'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAdminUser, )
