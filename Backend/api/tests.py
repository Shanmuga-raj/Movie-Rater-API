import json
from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Movie


class MovieTestCase(TestCase):
	def setUp(self) -> None:
		Movie.objects.create(title='Movie Title',
			description='Movie Description')

	def tearDown(self) -> None:
		Movie.objects.all().delete()

	def test_movie_str(self):
		movie = Movie.objects.get(id=1)
		expected_title = movie.title
		self.assertEqual(str(movie), expected_title)

	def test_post_new_movie(self):
		response = self.client.post('/api/movies/', {
					"title": "Django unchanined", 
					"description": "Django unchained is based on true story!.\
					Raw, Suspensful, Hate speech."})
		self.assertEqual(response.status_code, 201)

	def test_edit_movie(self):
		data = json.dumps({'title': 'Movie Title', 'description': 'Updated Movie Description'})
		response = self.client.put('/api/movies/1/', data, content_type='application/json')
		self.assertEqual(response.status_code, 200)


class UserTestCase(TestCase):
	def setUp(self) -> None:
		User.objects.create_user('fakeuser','user@fake.com','F@keU$Er')
		self.client = Client()

	def tearDown(self) -> None:
		User.objects.get(username='fakeuser').delete()

	def test_username(self):
		user = User.objects.get(id=1)
		expected_name = user.username
		self.assertEqual(str(user), expected_name)

	def test_known_user(self):
		login = self.client.login(username='fakeuser', password='F@keU$Er')
		self.assertTrue(login)

	def test_unknown_user(self):
		login = self.client.login(username='fakeuser2', password='abcdef')
		self.assertFalse(login)
