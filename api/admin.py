from django.contrib import admin
from .models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'description')
	list_filter = ('title', )
	list_per_page = 10
#	readonly_fields = ('title', )
	search_fields = ('title', )


class RatingAdmin(admin.ModelAdmin):
	autocomplete_fields = ('user', 'movie')
	list_display = ('id', 'movie', 'user', 'stars')
	list_editable = ('stars',)
	list_filter = ('stars',)
	search_fields = ('user__username', 'movie__title')


admin.site.register(Rating, RatingAdmin)
