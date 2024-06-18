from django.contrib import admin
from .models import Director, Movie, Review, Stars

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Stars)