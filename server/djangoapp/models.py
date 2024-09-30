# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, default='Unknown')  # Country where the make is based
    established_year = models.IntegerField(null=True, blank=True)  # Year when the make was established
    logo_url = models.URLField(max_length=200, null=True, blank=True)  # URL to the logo of the car make   
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupe'),
        ('SPORT', 'Sport'),

        
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    color = models.CharField(max_length=50, default='Unknown')  # Color of the car 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Price of the car model
    horsepower = models.IntegerField(null=True, blank=True)
       
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation
# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
