from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Movie(models.Model):
	title = models.CharField(max_length=32)
	description = models.TextField(max_length=320)

	def __str__(self) -> str:
		return self.title


class Rating(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stars = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])

	class Meta:
		unique_together = (('user', 'movie'),)
		index_together = (('user', 'movie'),)

	def __str__(self) -> str:
		return self.movie