from django.db import models


class Stars(models.Model):
    star = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.star)


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    duration = models.PositiveIntegerField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    stars = models.ForeignKey(Stars, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title} - {self.stars} Stars"