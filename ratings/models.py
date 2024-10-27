from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

    
def validate_Score(value):
    if value < 1 or value > 5 :
        raise ValidationError(f'rating must be between 1 and 5. You provided {value}')
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
   

    def __str__(self):
        return self.name

class Rating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    class Meta:
        unique_together = ('user', 'restaurant')

    def __str__(self):
        return f"{self.user.username} -{self.restaurant.name}: {self.score}"


