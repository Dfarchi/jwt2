from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Flight(models.Model):

    flight_number = models.CharField(max_length=256, db_column='flight num', null=False)
    origin_country = models.CharField(max_length=256, db_column='origin country', null=False)
    origin_city = models.CharField(max_length=256, db_column='origin city', null=False)
    origin_airport_code = models.CharField(max_length=5, db_column='origin airport', null=False)
    destination_country = models.CharField(max_length=256, db_column='destination country', null=False)
    destination_city = models.CharField(max_length=256, db_column='destination city', null=False)
    destination_airport_code = models.CharField(max_length=5, db_column='destination airport', null=False)
    date_origin = models.DateTimeField(db_column='date origin',null=False)
    date_destination = models.DateTimeField(db_column='date destination', null=False)
    seats = models.IntegerField(db_column='seats', null=False)
    Seats_left = models.IntegerField(db_column='seats left', null=False)
    is_cancelled= models.BooleanField(default='True',db_column='status', null=False)
    price = models.FloatField(default='0',db_column='price', null=False)


    class Meta:
        db_table = 'flights'

class Order(models.Model):

    user_is = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.IntegerField(default=1, db_column='seats', null=False)
    order_date = models.DateTimeField(db_column='date of order')
    price = models.FloatField(default='0', db_column='total price', null=False)

    class Meta:
        db_table = 'orders'
