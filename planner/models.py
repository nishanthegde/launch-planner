from django.db import models

class Movie(models.Model):
    movie_id = models.CharField(max_length=100)
    movie_desc = models.TextField()
    launch_date = models.DateField()
    complexity_score = models.IntegerField()
    popularity_score = models.FloatField()

    def __str__(self):
        return self.movie_desc

    class Meta:
        ordering = ['movie_id']

