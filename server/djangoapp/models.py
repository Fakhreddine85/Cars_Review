from django.db import models
from django.utils.timezone import now


# Create your models here.
class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)
    def __str__(self):
        return self.Name
# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarModel(models.Model):
    carMake = models.ForeignKey(CarMake,on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Dealer_id = models.IntegerField()
    class TypeChoices(models.TextChoices):
        SEDAN = '1', "Sedan"
        SUV = '2', "Suv"
        WAGON = '3', "Wagon"
    Type = models.CharField(max_length=30,choices=TypeChoices.choices,default=TypeChoices.SEDAN) 
    Year = models.DateField()
    def __str__(self):
        return self.Name

# <HINT> Create a Car Model model `class CarModel(models.Model):
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
#class CarDealer (models.Model):

# <HINT> Create a plain Python class `DealerReview` to hold review data
#class DealerReview (models.Model):
