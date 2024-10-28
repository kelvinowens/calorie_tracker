from django.db import models

class FoodEntry(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.calories} cal"
