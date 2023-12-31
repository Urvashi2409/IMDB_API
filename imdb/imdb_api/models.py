from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class StreamPlatform(models.Model):

    name = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class Watchlist(models.Model):

    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=100)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# single watchlist contains multiple reviews 
class Review(models.Model):
    
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=100)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        string = str(self.rating) + " " + str(self.watchlist.title)
        return string 