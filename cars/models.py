from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Car(models.Model):
    Make_Name = models.CharField(max_length=255, blank=False, null=False)
    Model_Name = models.CharField(max_length=500, blank=False, null=False)

    class Meta:
        unique_together = (('Make_Name', 'Model_Name'),)

    @property
    def avg_rating(self):
        return self.ratings.aggregate(avg_rating=models.Avg('Rate_Value'))['avg_rating']
    
    def __str__(self) -> str:
        return f"ID: {self.pk}    Make: {self.Make_Name}    Model: {self.Model_Name}"


class Rating(models.Model):
    Car = models.ForeignKey(Car, related_name="ratings", on_delete=models.CASCADE)
    Rate_Value = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    def __str__(self) -> str:
        return f"Car_ID: {self.Car.pk}    Rating: {self.Rate_Value}"